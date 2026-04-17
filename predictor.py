def analyze_match(team1, team2, t1, t2):

    # attacking strength
    t1_attack = t1["avg_scored"]
    t2_attack = t2["avg_scored"]

    # defensive weakness
    t1_def = t1["avg_conceded"]
    t2_def = t2["avg_conceded"]

    # expected goals (real logic)
    team1_xg = (t1_attack + t2_def) / 2
    team2_xg = (t2_attack + t1_def) / 2

    total_goals = team1_xg + team2_xg

    over_25 = min(95, total_goals * 30)
    btts = min(95, (team1_xg * team2_xg) * 25)

    team1_win = 50 + (t1["win_rate"] - t2["win_rate"]) * 80
    team2_win = 100 - team1_win

    confidence = (over_25 * 0.4 + btts * 0.3 + max(team1_win, team2_win) * 0.3)

    if over_25 > btts and over_25 > team1_win:
        pick = "Over 2.5"
    elif btts > team1_win:
        pick = "BTTS Yes"
    else:
        pick = f"{team1 if team1_win > team2_win else team2} Win"

    return {
        "Pick": pick,
        "Confidence%": round(confidence, 1),
        "Over2.5%": round(over_25, 1),
        "BTTS%": round(btts, 1),
        "Score": f"{round(team1_xg)}-{round(team2_xg)}"
    }
