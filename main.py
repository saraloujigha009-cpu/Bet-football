import schedule
import time

from scheduler import send_morning_bets, send_live_bets

schedule.every().day.at("09:00").do(send_morning_bets)

schedule.every().day.at("19:00").do(send_live_bets)

print("BetBot running...")

while True:
    schedule.run_pending()
    time.sleep(60)
