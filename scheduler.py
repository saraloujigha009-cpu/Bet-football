from api import get_today_matches
from predictor import analyze_match
from telegram import Bot
import requests

TOKEN = "8754438460:AAEliYNcIBCu9eb26oy8b7kXPoEqiHZhuVg"
CHAT_ID = "8797710776"
API_KEY = "bc2df9e4ea817767c164df0b13d1f24b"

bot = Bot(token=TOKEN)


def send_morning_bets():

    matches = get_today_matches()

    bets = []

    for m in matches:

        r = analyze_match(m["team1"], m["team2"], 1.5, 1.3)

        if r["Confidence%"] >= 85:
            bets.append((m, r))

    bets.sort(key=lambda x: x[1]["Confidence%"], reverse=True)

    top3 = bets[:3]

    msg = "🔥 MORNING FIXED BETS\n\n"

    for i,(m,r) in enumerate(top3,1):

        msg += f"""
{i}) {m['team1']} vs {m['team2']}
Pick: {r['Pick']}
Confidence: {r['Confidence%']}%
Score: {r['Score']}

"""

    bot.send_message(chat_id=CHAT_ID,text=msg)


def send_live_bets():

    url = "https://v3.football.api-sports.io/fixtures?live=all"

    headers = {
        "x-apisports-key": API_KEY
    }

    r = requests.get(url,headers=headers)

    data = r.json()

    bets = []

    for m in data["response"]:

        team1 = m["teams"]["home"]["name"]
        team2 = m["teams"]["away"]["name"]

        r = analyze_match(team1,team2,1.7,1.5)

        if r["Confidence%"] >= 87:
            bets.append((team1,team2,r))

    bets.sort(key=lambda x: x[2]["Confidence%"], reverse=True)

    top3 = bets[:3]

    msg = "⚡ LIVE BETS\n\n"

    for i,(t1,t2,r) in enumerate(top3,1):

        msg += f"""
{i}) {t1} vs {t2}
Pick: {r['Pick']}
Confidence: {r['Confidence%']}%
Score: {r['Score']}

"""

    bot.send_message(chat_id=CHAT_ID,text=msg)
