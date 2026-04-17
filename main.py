from predictor import predict_match
from api import matches, get_team_form

for match in matches:

    team1_form = get_team_form(match["team1_id"])
    team2_form = get_team_form(match["team2_id"])

    result = predict_match(
        team1_form[0],
        team2_form[0]
    )

    print(match["team1"], "vs", match["team2"], "=>", result)
