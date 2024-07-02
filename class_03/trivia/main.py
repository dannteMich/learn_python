import pathlib
import json
import random
import argparse

from question import Question
from player import Player
from validated_question import ValidatedQuestion


def get_questions_from_file(file_path: str):
    questions_file = pathlib.Path(file_path)
    assert questions_file.exists(), "File does not exist"
    questions_list = json.load(questions_file.open())

    game_questions = [ValidatedQuestion.model_validate(q) for q in questions_list]
    random.shuffle(game_questions)
    return game_questions


def game_question_from_validated_question(q: ValidatedQuestion):
    answers = q.incorrectAnswers + [q.correctAnswer]
    random.shuffle(answers)
    correct_index = answers.index(q.correctAnswer)

    return Question(q.question, answers, correct_index, q.difficulty)


def build_parser():
    parser = argparse.ArgumentParser(description="Play a trivia game")
    parser.add_argument(
        "questions_path", help="Path to a json file with questions", type=pathlib.Path
    )
    parser.add_argument("player", nargs="+", help="Names of players")
    parser.add_argument(
        "--max-questions", "-m", help="max number of questions", type=int, default=None
    )

    return parser


def validate_arguments(args):
    if not args.questions_path.is_file():
        raise ValueError(f"file {args.questions_path} is not an existing file")
    if args.max_questions is not None and args.max_questions <= 0:
        raise ValueError("You have to have at least 1 as the max number of questions")


def print_score(players: list[Player]):
    for player in players:
        print(f"{player.name}: {player.score}")

if __name__ == "__main__":

    parser = build_parser()
    args = parser.parse_args()
    validate_arguments(args)

    questions_data = get_questions_from_file(args.questions_path)
    
    players = [Player(player) for player in args.player]
    all_questions = [game_question_from_validated_question(q) for q in questions_data]
    game_questions = all_questions[: args.max_questions]

    print("Starting Game")

    while len(game_questions) > 0:
        current_question = game_questions[0]
        current_player = players.pop(0)

        print(f"{current_player.name}, it's your turn")
        if current_question.ask_a_question():
            print("Great")
            current_player.increase_score(current_question.difficulty)
            game_questions.pop(0)
        else:
            print("Fail!!!! Great Fail")

        players.append(current_player)

    print_score(players)    
