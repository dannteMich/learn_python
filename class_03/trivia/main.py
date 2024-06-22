import pathlib
import json
import random

from question import Question


def get_questions_from_file(file_path: str):
    questions_file = pathlib.Path(file_path)
    assert questions_file.exists(), "File does not exist"
    questions_list = json.load(questions_file.open())

    game_questions = [
        Question(q["question"], q["answers"], q["correct_answer_index"])
        for q in questions_list
    ]

    return game_questions


if __name__ == "__main__":
    print("Starting Game")

    game_questions = get_questions_from_file("questions.json")
    random.shuffle(game_questions)

    for q in game_questions[:3]:
        if q.ask_a_question():
            print("Great")
        else:
            print("Fail!!!! Great Fail")
