from api import get_matches, get_form
from predictor import analyze_match
from bot import send_message

matches = get_matches()

bets = []

for m in matches:

    t1 = get_form(m["team1_id"])
    t2 = get_form(m["team2_id"])

    result = analyze_match(m["team1"], m["team2"], t1, t2)

    if result["Confidence%"] >= 80:
        bets.append({
            "match": f"{m['team1']} vs {m['team2']}",
            "result": result
        })

bets.sort(key=lambda x: x["result"]["Confidence%"], reverse=True)

top3 = bets[:3]

msg = "🔥 AI BETS (REAL MODEL)\n\n"

for i, b in enumerate(top3, 1):
    r = b["result"]
    msg += f"""
{i}. {b['match']}
Pick: {r['Pick']}
Confidence: {r['Confidence%']}%
Score: {r['Score']}
"""

send_message(msg)
