from api import get_today_matches, get_team_stats
from predictor import analyze_match
from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    matches = get_today_matches()

    bets = []
    used_picks = set()  # 🧠 باش ما يتكرروش نفس type

    for m in matches[:15]:

        try:
            stats1 = get_team_stats(m["team1_id"])
            stats2 = get_team_stats(m["team2_id"])

            result = analyze_match(m["team1"], m["team2"], stats1, stats2)

            pick = result["Pick"]

            # 🧠 منع التكرار
            if pick in used_picks:
                continue

            if result["Confidence"] >= 60:

                bets.append({
                    "team1": m["team1"],
                    "team2": m["team2"],
                    "pick": pick,
                    "confidence": result["Confidence"]
                })

                used_picks.add(pick)

        except:
            continue

    bets = sorted(bets, key=lambda x: x["confidence"], reverse=True)[:3]

    if not bets:
        await update.message.reply_text("⚠️ No strong bets today")
        return

    msg = "🔥 SMART VALUE BETS (PRO MODE)\n\n"

    for i, b in enumerate(bets, 1):

        msg += f"""
{i}) {b['team1']} vs {b['team2']}
Prediction: {b['pick']}
Confidence: {b['confidence']}%
"""

    await update.message.reply_text(msg)
