from telegram import Bot
import time

TOKEN = "8754438460:AAEliYNcIBCu9eb26oy8b7kXPoEqiHZhuVg"
CHAT_ID = "PUT_YOUR_CHAT_ID"

bot = Bot(token=TOKEN)

def send_message(text):
    bot.send_message(chat_id=CHAT_ID, text=text)
