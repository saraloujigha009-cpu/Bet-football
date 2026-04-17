from telegram import Bot

TOKEN = "8754438460:AAEliYNcIBCu9eb26oy8b7kXPoEqiHZhuVg"
CHAT_ID = 8797710776

bot = Bot(token=TOKEN)

bot.send_message(chat_id=CHAT_ID, text="🔥 Test message from BetBot")
