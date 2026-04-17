import random

def analyze_match(team1, team2):

    attack1 = random.uniform(1.2, 2.4)
    attack2 = random.uniform(1.0, 2.2)

    total = attack1 + attack2

    if total >= 3:
        pick = "Over 2.5"
    elif attack1 > attack2:
        pick = f"{team1} Win"
    else:
        pick = f"{team2} Win"

    confidence = round(random.uniform(86, 92), 1)

    score_prediction = f"{round(attack1)}-{round(attack2)}"

    return {
        "Pick": pick,
        "Confidence": confidence,
        "Score": score_prediction
    }
