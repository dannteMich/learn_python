import pathlib
import json
import random

from question import Question
from validated_question import ValidatedQuestion


def get_questions_from_file(file_path: str):
    questions_file = pathlib.Path(file_path)
    assert questions_file.exists(), "File does not exist"
    questions_list = json.load(questions_file.open())

    game_questions = [ValidatedQuestion.model_validate(q) for q in questions_list]

    return game_questions


def game_question_from_validated_question(q: ValidatedQuestion):
    answers = q.incorrectAnswers + [q.correctAnswer]
    random.shuffle(answers)
    correct_index = answers.index(q.correctAnswer)

    return Question(q.question, answers, correct_index)


if __name__ == "__main__":
    print("Starting Game")

    questions_data = get_questions_from_file("extended_questions.json")
    random.shuffle(questions_data)

    game_questions = [game_question_from_validated_question(q) for q in questions_data]

    for q in game_questions[:3]:
        if q.ask_a_question():
            print("Great")
        else:
            print("Fail!!!! Great Fail")
