from api import get_today_matches
from predictor import analyze_match
from telegram import Bot
from config import TELEGRAM_TOKEN, CHAT_ID

bot = Bot(token=TELEGRAM_TOKEN)

def send_morning_bets():

    matches = get_today_matches()

    bets = []

    for m in matches:

        result = analyze_match(m["team1"], m["team2"])

        if result["Confidence"] >= 86:

            bets.append({
                "team1": m["team1"],
                "team2": m["team2"],
                "league": m["league"],
                "pick": result["Pick"],
                "confidence": result["Confidence"],
                "score": result["Score"]
            })

    bets = sorted(bets, key=lambda x: x["confidence"], reverse=True)

    top3 = bets[:3]

    msg = "🔥 MORNING FIXED BETS\n\n"

    for i, b in enumerate(top3, 1):

        msg += f"""
{i}) {b['team1']} vs {b['team2']}
League: {b['league']}
Pick: {b['pick']}
Confidence: {b['confidence']}%
Score: {b['score']}

"""

    bot.send_message(chat_id=CHAT_ID, text=msg)
