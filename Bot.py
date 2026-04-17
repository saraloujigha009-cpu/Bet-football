from api import get_today_matches, get_team_stats
from predictor import analyze_match
from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    matches = get_today_matches()

    bets = []

    for m in matches[:15]:

        stats1 = get_team_stats(m["team1_id"])
        stats2 = get_team_stats(m["team2_id"])

        result = analyze_match(m["team1"], m["team2"], stats1, stats2)

        if result["Confidence"] >= 75:

            bets.append({
                "team1": m["team1"],
                "team2": m["team2"],
                "pick": result["Pick"],
                "confidence": result["Confidence"],
                "score": result["Score"]
            })

    bets = sorted(bets, key=lambda x: x["confidence"], reverse=True)[:3]

    msg = "🔥 PRO VALUE BETS (REAL DATA)\n\n"

    for i, b in enumerate(bets, 1):

        msg += f"""
{i}) {b['team1']} vs {b['team2']}
Pick: {b['pick']}
Confidence: {b['confidence']}%
Score: {b['score']}
"""

    await update.message.reply_text(msg)
