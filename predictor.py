def predict_match(team1_goals_avg, team2_goals_avg):
    total_goals = team1_goals_avg + team2_goals_avg

    # Over 2.5 logic
    if total_goals >= 2.8:
        return "Over 2.5"

    # BTTS logic
    if team1_goals_avg > 0.8 and team2_goals_avg > 0.8:
        return "BTTS Yes"

    # fallback winner
    if team1_goals_avg > team2_goals_avg:
        return "Team 1 Win"
    else:
        return "Team 2 Win"
