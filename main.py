from telegram.ext import ApplicationBuilder, CommandHandler
from config import TELEGRAM_TOKEN
from bot import start


app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("🔥 BOT RUNNING...")

app.run_polling()
