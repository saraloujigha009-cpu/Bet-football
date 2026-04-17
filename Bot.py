from api import get_today_matches, get_team_stats, get_match_odds
from predictor import analyze_match
from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    matches = get_today_matches()

    bets = []
    used = set()

    for m in matches[:20]:

        try:
            stats1 = get_team_stats(m["team1_id"])
            stats2 = get_team_stats(m["team2_id"])

            odds = get_match_odds(m["fixture_id"])

            result = analyze_match(
                m["team1"],
                m["team2"],
                stats1,
                stats2,
                odds
            )

            pick = result["Pick"]

            if pick in used:
                continue

            if result["Confidence"] >= 65 and result["Value"] > 0:

                bets.append({
                    "team1": m["team1"],
                    "team2": m["team2"],
                    "pick": pick,
                    "confidence": result["Confidence"],
                    "value": result["Value"]
                })

                used.add(pick)

        except:
            continue

    bets = sorted(bets, key=lambda x: x["value"], reverse=True)[:3]

    if not bets:
        await update.message.reply_text("⚠️ No positive value bets today")
        return

    msg = "🔥 ELITE VALUE BETTING SYSTEM\n\n"

    for i, b in enumerate(bets, 1):

        msg += f"""
{i}) {b['team1']} vs {b['team2']}
Prediction: {b['pick']}
Value: {b['value']}%
Confidence: {b['confidence']}%
"""

    await update.message.reply_text(msg)
