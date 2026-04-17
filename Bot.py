from api import get_today_matches, get_team_stats
from predictor import analyze_match
from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        matches = get_today_matches()
    except:
        await update.message.reply_text("❌ API error: cannot fetch matches")
        return

    if not matches:
        await update.message.reply_text("⚠️ No matches available today")
        return

    bets = []

    for m in matches:

        try:
            stats1 = get_team_stats(m["team1_id"])
            stats2 = get_team_stats(m["team2_id"])

            # 🛡️ حماية من null / None
            if not stats1 or not stats2:
                continue

            if "goals_for" not in stats1 or "goals_for" not in stats2:
                continue

            result = analyze_match(
                m["team1"],
                m["team2"],
                stats1,
                stats2
            )

            if result and result.get("Confidence", 0) >= 82:

                bets.append({
                    "team1": m["team1"],
                    "team2": m["team2"],
                    "pick": result["Pick"],
                    "confidence": result["Confidence"],
                    "score": result["Score"]
                })

        except Exception as e:
            print("Match error:", e)
            continue

    # 🛡️ إذا ماكاين حتى bet صالح
    if len(bets) == 0:
        await update.message.reply_text("⚠️ No strong bets found (low confidence data)")
        return

    bets = sorted(bets, key=lambda x: x["confidence"], reverse=True)[:3]

    msg = "🔥 TODAY TOP SAFE BETS\n\n"

    for i, b in enumerate(bets, 1):

        msg += f"""
{i}) {b['team1']} vs {b['team2']}
Pick: {b['pick']}
Confidence: {b['confidence']}%
Score: {b['score']}
"""

    await update.message.reply_text(msg)
