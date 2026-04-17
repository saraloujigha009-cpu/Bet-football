from predictor import predict_match
from data import matches

for match in matches:
    result = predict_match(
        match["team1_avg_goals"],
        match["team2_avg_goals"]
    )

    print(f"{match['team1']} vs {match['team2']} ➜ {result}")
