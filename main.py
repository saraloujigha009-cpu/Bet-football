from predictor import predict_match
from api import get_matches

matches = get_matches()

for match in matches:

    result = predict_match(
        match["team1_form"][0],
        match["team2_form"][0]
    )

    print("\n", match["team1"], "vs", match["team2"])
    print(result)
