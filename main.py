import threading
import time

from bot import app  # telegram bot
from scheduler import send_daily_bet

# 🟢 تشغيل auto mode كل 24h
def auto_loop():
    while True:
        send_daily_bet()
        time.sleep(86400)  # 24h

# تشغيل thread ديال auto
threading.Thread(target=auto_loop).start()

# تشغيل bot (chat mode)
print("🔥 Bot running 24/7...")
app.run_polling()
