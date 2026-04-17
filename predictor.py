def predict_match(team1_goals, team2_goals):

    total = team1_goals + team2_goals

    # Over 2.5 probability
    over_25 = min(95, max(5, total * 35))

    # BTTS probability
    btts = min(95, max(5, (team1_goals * team2_goals) * 40))

    # Win probability (simple model)
    team1_win = 50 + (team1_goals - team2_goals) * 20
    team2_win = 100 - team1_win

    # pick best bet
    if over_25 > 65:
        pick = "Over 2.5"
    elif btts > 60:
        pick = "BTTS Yes"
    else:
        pick = "Winner"

    return {
        "Over2.5%": round(over_25, 1),
        "BTTS%": round(btts, 1),
        "Team1Win%": round(team1_win, 1),
        "Team2Win%": round(team2_win, 1),
        "Pick": pick
    }
