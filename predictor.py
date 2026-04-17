def predict_match(team1_goals, team2_goals):

    total = team1_goals + team2_goals

    over_25 = min(95, max(5, total * 35))
    btts = min(95, max(5, (team1_goals * team2_goals) * 40))

    team1_win = 50 + (team1_goals - team2_goals) * 20
    team2_win = 100 - team1_win

    # Confidence = strength of best prediction
    confidence = (
    over_25 * 0.4 +
    btts * 0.3 +
    max(team1_win, team2_win) * 0.3
    )
    
    if result["Confidence%"] >= 85 and result["Score"] != "1-1":
    if over_25 == confidence:
        pick = "Over 2.5"
    elif btts == confidence:
        pick = "BTTS Yes"
    elif team1_win > team2_win:
        pick = "Team 1 Win"
    else:
        pick = "Team 2 Win"

    return {
        "Over2.5%": round(over_25, 1),
        "BTTS%": round(btts, 1),
        "Team1Win%": round(team1_win, 1),
        "Team2Win%": round(team2_win, 1),
        "Confidence%": round(confidence, 1),
        "Pick": pick
    }
