from predictor import predict_match
from api import get_matches
from api import get_team_form

matches = get_matches()

for match in matches:

    team1_form = get_team_form(match["team1_id"])
    team2_form = get_team_form(match["team2_id"])

    result = predict_match(
        team1_form[0],
        team2_form[0]
    )

    print(f"{match['team1']} vs {match['team2']} => {result}")
