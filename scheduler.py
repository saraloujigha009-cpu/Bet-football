import time
from api import get_matches
from predictor import analyze_match
from bot import send_message

def send_daily_bet():

    matches = get_matches()
    best = None

    for m in matches:

        result = analyze_match(
            m["team1"],
            m["team2"],
            m["team1_form"][0],
            m["team2_form"][0]
        )

        if result["Confidence%"] >= 70:
            best = (m, result)
            break

    if best:
        m, r = best

        msg = f"""
🔥 DAILY BEST BET

{m['team1']} vs {m['team2']}

Pick: {r['Pick']}
Confidence: {r['Confidence%']}%
Score: {r['Score']}
"""

        send_message(msg)

        print("Daily bet sent ✔️")
