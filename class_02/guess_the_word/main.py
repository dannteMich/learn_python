import pathlib
import random
import json

from word_game import guess_the_word_and_update_players


def get_words_and_descriptions():
    current_file_path = pathlib.Path(__file__)
    words_path = current_file_path.parent / "words.json"
    words_for_game = json.loads(words_path.read_text())
    random.shuffle(words_for_game)

    return words_for_game


def create_players_array(number_of_players: int):
    players = []
    for i in range(number_of_players):
        player_name = f"player_{i+1}"
        players.append((player_name, 0))

    return players


if __name__ == "__main__":
    print("Starting Game\n")

    words_for_game = get_words_and_descriptions()
    players = create_players_array(3)

    for guess_dict in words_for_game:
        guess_the_word_and_update_players(guess_dict, players)

    print("\nGame is over. Score:")
    for player_name, score in players:
        print(f"{player_name} : {score}")
