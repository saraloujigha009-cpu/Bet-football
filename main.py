from api import get_matches
from predictor import predict_match
from bot import send_message

matches = get_matches()

best_bet = None

for match in matches:

    result = predict_match(
        match["team1_form"][0],
        match["team2_form"][0]
    )

    if result["Confidence%"] >= 70:
        best_bet = (match, result)
        break

if best_bet:

    match, result = best_bet

    message = f"""
🔥 BEST BET TODAY 🔥

{match['team1']} vs {match['team2']}

Pick: {result['Pick']}
Confidence: {result['Confidence%']}%

Over2.5: {result['Over2.5%']}%
BTTS: {result['BTTS%']}%
"""

    send_message(message)

    print("Message sent!")
else:
    print("No strong bets today")
