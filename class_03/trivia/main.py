import pathlib
import argparse

from player import Player
from questions_collection import QuestionCollection


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


def main():
    parser = build_parser()
    args = parser.parse_args()
    validate_arguments(args)

    players = [Player(player) for player in args.player]

    questions = QuestionCollection.build_from_file(
        args.questions_path, args.max_questions
    )

    print("Starting Game")
    while len(questions) > 0:
        current_question = questions.pop_question_by_category()
        current_player = players.pop(0)

        print(f"{current_player.name}, it's your turn")
        if current_question.ask_a_question():
            print("Great")
            current_player.increase_score(current_question.difficulty)
        else:
            print("Fail!!!! Great Fail")

        players.append(current_player)

    print_score(players)


def validate_arguments(args):
    if not args.questions_path.is_file():
        raise ValueError(f"file {args.questions_path} is not an existing file")
    if args.max_questions is not None and args.max_questions <= 0:
        raise ValueError("You have to have at least 1 as the max number of questions")


def print_score(players: list[Player]):
    for player in players:
        print(f"{player.name}: {player.score}")


if __name__ == "__main__":
    main()
