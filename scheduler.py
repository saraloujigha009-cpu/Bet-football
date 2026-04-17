import requests
from datetime import datetime
from predictor import analyze_match
from telegram import Bot

TOKEN = "8754438460:AAEliYNcIBCu9eb26oy8b7kXPoEqiHZhuVg"
CHAT_ID = "8797710776"
API_KEY = "bc2df9e4ea817767c164df0b13d1f24b"

bot = Bot(token=TOKEN)


def get_matches_today():

    today = datetime.today().strftime('%Y-%m-%d')

    url = f"https://v3.football.api-sports.io/fixtures?date={today}"

    headers = {
        "x-apisports-key": API_KEY
    }

    r = requests.get(url, headers=headers)
    data = r.json()

    matches = []

    for m in data["response"]:

        team1 = m["teams"]["home"]["name"]
        team2 = m["teams"]["away"]["name"]

        matches.append({
            "team1": team1,
            "team2": team2
        })

    return matches


# 🟢 3 BETS MORNING
def send_morning_bets():

    matches = get_matches_today()
    bets = []

    for m in matches:

        result = analyze_match(m["team1"], m["team2"], 1.5, 1.3)

        if result["Confidence%"] >= 85:
            bets.append((m, result))

    bets.sort(key=lambda x: x[1]["Confidence%"], reverse=True)

    top3 = bets[:3]

    msg = "🔥 MORNING FIXED BETS\n\n"

    for i, (m, r) in enumerate(top3, 1):

        msg += f"""
{i}) {m['team1']} vs {m['team2']}
Pick: {r['Pick']}
Confidence: {r['Confidence%']}%
Score: {r['Score']}

"""

    bot.send_message(chat_id=CHAT_ID, text=msg)


# 🔴 3 LIVE BETS EVENING
def send_live_bets():

    matches = get_matches_today()
    bets = []

    for m in matches:

        result = analyze_match(m["team1"], m["team2"], 1.8, 1.6)

        if result["Confidence%"] >= 87:
            bets.append((m, result))

    bets.sort(key=lambda x: x[1]["Confidence%"], reverse=True)

    top3 = bets[:3]

    msg = "⚡ LIVE BETS EVENING\n\n"

    for i, (m, r) in enumerate(top3, 1):

        msg += f"""
{i}) {m['team1']} vs {m['team2']}
Pick: {r['Pick']}
Confidence: {r['Confidence%']}%
Score: {r['Score']}

"""

    bot.send_message(chat_id=CHAT_ID, text=msg)
