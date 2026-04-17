import schedule
import time

from scheduler import send_morning_bets
from scheduler import send_evening_bets


# 🟢 3 مباريات فالصباح
schedule.every().day.at("09:00").do(send_morning_bets)

# 🔴 3 مباريات فالمساء
schedule.every().day.at("19:00").do(send_evening_bets)

print("BetBot running...")

while True:
    schedule.run_pending()
    time.sleep(60)
