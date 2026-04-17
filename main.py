import schedule
import time
from scheduler import send_daily_bets

# كل نهار فـ 09:00 صباحا
schedule.every().day.at("09:00").do(send_daily_bets)

print("BetBot running...")

while True:
    schedule.run_pending()
    time.sleep(60)
