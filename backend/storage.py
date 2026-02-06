import json
import os

FILE = "data.json"

def save_quiz(data):
    quizzes = []

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            quizzes = json.load(f)

    quizzes.append(data)

    with open(FILE, "w") as f:
        json.dump(quizzes, f, indent=2)

def get_all_quizzes():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r") as f:
        return json.load(f)

