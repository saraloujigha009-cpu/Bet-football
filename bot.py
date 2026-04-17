from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8754438460:AAEliYNcIBCu9eb26oy8b7kXPoEqiHZhuVg"

# 🟢 START
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bot started successfully")

# 🟢 CHAT ANALYSIS
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if not text or text.startswith("/start"):
        return

    if "vs" not in text.lower():
        await update.message.reply_text("❌ Use format: Team A vs Team B")
        return

    team1, team2 = text.split("vs")

    msg = f"""
🔥 MATCH ANALYSIS

{team1.strip()} vs {team2.strip()}

Pick: Over 2.5
Confidence: 80%
Score: 2-1
"""

    await update.message.reply_text(msg)

# 🟢 INIT APP
def create_app():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    return app
