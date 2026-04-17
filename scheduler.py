from api import get_matches
from predictor import analyze_match
from bot import create_app
from telegram import Bot

TOKEN = "YOUR_TOKEN"
bot = Bot(token=TOKEN)

def send_daily_bets():

    matches = get_matches()
    bets = []

    for m in matches:

        result = analyze_match(
            m["team1"],
            m["team2"],
            m["team1_form"][0],
            m["team2_form"][0]
        )

        if result["Confidence%"] >= 80:
            bets.append((m, result))

    bets.sort(key=lambda x: x[1]["Confidence%"], reverse=True)
    top3 = bets[:3]

    if not top3:
        bot.send_message(chat_id=8797710776, text="❌ No strong bets today")
        return

    msg = "🔥 TODAY BEST 3 BETS\n\n"

    for i, (m, r) in enumerate(top3, 1):
        msg += f"""
{i}. {m['team1']} vs {m['team2']}
Pick: {r['Pick']}
Confidence: {r['Confidence%']}%
Score: {r['Score']}
"""

    bot.send_message(chat_id=8797710776, text=msg)
