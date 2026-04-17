from api import get_today_matches, get_team_stats
from predictor import analyze_match
from telegram import Bot
from config import TELEGRAM_TOKEN, CHAT_ID

bot = Bot(token=TELEGRAM_TOKEN)


def send_morning_bets():

    matches = get_today_matches()
    bets = []

    for m in matches:

        stats1 = get_team_stats(m["team1_id"])
        stats2 = get_team_stats(m["team2_id"])

        result = analyze_match(m["team1"], m["team2"], stats1, stats2)

        if result["Confidence"] >= 85:

            bets.append({
                "team1": m["team1"],
                "team2": m["team2"],
                "league": m["league"],
                "pick": result["Pick"],
                "confidence": result["Confidence"],
                "score": result["Score"]
            })

    bets = sorted(bets, key=lambda x: x["confidence"], reverse=True)[:3]

    msg = "🔥 MORNING FIXED BETS\n\n"

    for i, b in enumerate(bets, 1):

        msg += f"""
{i}) {b['team1']} vs {b['team2']}
League: {b['league']}
Pick: {b['pick']}
Confidence: {b['confidence']}%
Score: {b['score']}
"""

    bot.send_message(chat_id=CHAT_ID, text=msg)
