from predictor import predict_match
from api import get_matches

matches = get_matches()

best_bets = []

for match in matches:

    result = predict_match(
        match["team1_form"][0],
        match["team2_form"][0]
    )

    if result["Confidence%"] >= 70:
        best_bets.append({
            "match": f"{match['team1']} vs {match['team2']}",
            "data": result
        })

# ترتيب من الأقوى للأضعف
best_bets.sort(key=lambda x: x["data"]["Confidence%"], reverse=True)

# نخليو غير top 1
if best_bets:
    top = best_bets[0]

    print("\n🔥 BEST BET TODAY 🔥")
    print(top["match"])
    print(top["data"])
else:
    print("❌ No strong bets today")
