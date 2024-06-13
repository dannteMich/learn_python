from pathlib import Path
import random
import json
from argparse import ArgumentParser, Namespace

from word_game import guess_the_word_and_update_players


def parse_words_and_descriptions_from_file(words_path: Path):

    words_for_game = json.loads(words_path.read_text())
    random.shuffle(words_for_game)

    return words_for_game


def create_players_array(player_names: list[str]):
    players = []
    for name in player_names:
        players.append((name, 0))

    return players


def build_parser():
    parser = ArgumentParser(description="This is a game for guessing words")
    parser.add_argument(
        "words_path", help="path to JSON file with words and descriptions"
    )
    parser.add_argument("player_name", help="names of the players", nargs="+")
    parser.add_argument("-l","--word-limit", type=int, help="Max number of words in the game", default=None)

    return parser

def validate_args(args: Namespace):
    words_path = Path(args.words_path)
    assert words_path.is_file()
    
    if args.word_limit is not None:
        assert args.word_limit > 0, "max words has to be at least 1"
    
    if len(args.player_name) < 2:
        print("You chose only one player - this is not going to be an interesting game")
    


if __name__ == "__main__":

    parser = build_parser()
    args = parser.parse_args()
    validate_args(args)
    
    words_path = Path(args.words_path)
    player_names = args.player_name

    players = create_players_array(player_names)
    words_for_game = parse_words_and_descriptions_from_file(words_path)
    if args.word_limit is not None and args.word_limit < len(words_for_game):
        words_for_game = words_for_game[:args.word_limit]

    print("Starting Game\n")
    for guess_dict in words_for_game:
        guess_the_word_and_update_players(guess_dict, players)

    print("\nGame is over. Score:")
    for player_name, score in players:
        print(f"{player_name} : {score}")
