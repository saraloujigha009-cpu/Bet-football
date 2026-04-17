from bot import create_app
from scheduler import send_daily_bets
import threading
import time

# 🟢 Auto mode (مرة فاليوم فقط)
def auto_loop():
    while True:
        send_daily_bets()
        time.sleep(86400)

# start auto thread
threading.Thread(target=auto_loop, daemon=True).start()

# start bot
app = create_app()

print("🔥 BetBot running clean version...")
app.run_polling()
