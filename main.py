import schedule
import time

from scheduler import send_morning_bets, send_evening_bets

# 🟢 صباح 09:00
schedule.every().day.at("09:00").do(send_morning_bets)

# 🔴 مساء 19:00
schedule.every().day.at("19:00").do(send_evening_bets)

print("🔥 BetBot is running 24/7...")

while True:
    schedule.run_pending()
    time.sleep(60)
