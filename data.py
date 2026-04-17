import json
import os

DB_FILE = "history.json"


def save_prediction(data):

    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump([], f)

    with open(DB_FILE, "r") as f:
        history = json.load(f)

    history.append(data)

    with open(DB_FILE, "w") as f:
        json.dump(history, f, indent=2)


def get_history():

    if not os.path.exists(DB_FILE):
        return []

    with open(DB_FILE, "r") as f:
        return json.load(f)
