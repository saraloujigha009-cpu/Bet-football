from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from api import get_today_matches
from scheduler import send_morning_bets
from predictor import analyze_match
from api import get_team_stats

TOKEN = "8754438460:AAEliYNcIBCu9eb26oy8b7kXPoEqiHZhuVg"


# 🟢 START يعطي مباشرة أفضل 3 مباريات
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    matches = get_today_matches()
    bets = []

    for m in matches:

        stats1 = get_team_stats(m["team1_id"])
        stats2 = get_team_stats(m["team2_id"])

        result = analyze_match(m["team1"], m["team2"], stats1, stats2)

        if result["Confidence"] >= 85:

            bets.append({
                "team1": m["team1"],
                "team2": m["team2"],
                "pick": result["Pick"],
                "confidence": result["Confidence"],
                "score": result["Score"]
            })

    bets = sorted(bets, key=lambda x: x["confidence"], reverse=True)[:3]

    msg = "🔥 TODAY TOP BETS\n\n"

    for i, b in enumerate(bets, 1):

        msg += f"""
{i}) {b['team1']} vs {b['team2']}
Pick: {b['pick']}
Confidence: {b['confidence']}%
Score: {b['score']}
"""

    await update.message.reply_text(msg)


# 🟢 أي رسالة فيها "vs"
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text.lower()

    if "vs" not in text:
        await update.message.reply_text("📌 Send format: Team A vs Team B")
        return

    try:
        team1, team2 = update.message.text.split("vs")

        team1 = team1.strip()
        team2 = team2.strip()

        # fake stats fallback (باش ما يطيحش)
        stats1 = {"goals_for": 1.5, "goals_against": 1.2}
        stats2 = {"goals_for": 1.3, "goals_against": 1.4}

        from predictor import analyze_match
        result = analyze_match(team1, team2, stats1, stats2)

        msg = f"""
⚽ MATCH ANALYSIS

{team1} vs {team2}

Pick: {result['Pick']}
Confidence: {result['Confidence']}%
Score: {result['Score']}
"""

        await update.message.reply_text(msg)

    except:
        await update.message.reply_text("❌ Error in format")


# 🟢 تشغيل البوت
def create_app():

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    return app
