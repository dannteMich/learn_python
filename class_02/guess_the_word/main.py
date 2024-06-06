def print_partial_word(word: str, guessed_letters: list[str]):
    res = ""
    for letter in word:
        if letter in guessed_letters:
            res = res + letter
        else:
            res = res + "*"

    print(res)


def get_single_letter_from_user(guessed_letters: list[str]) -> str:
    while True:
        letter = input("Please provide a single letter: ").upper()
        if len(letter) != 1:
            print("The input should be 1 letter. No more and no less")
        elif not letter.isalpha():
            print("The input should be only alphabetical letters")
        elif letter in guessed_letters:
            print("This letter was already guessed")
        else:
            return letter


def is_word_fully_guessed(word: str, guessed_letters: list[str]):
    for letter in word:
        if not letter in guessed_letters:
            return False

    return True


def guess_the_word_and_update_score(
    word_to_guess: str, current_player_index: int, players_score: list[int]
):
    """Returns the next player index to play"""

    word_to_guess = word_to_guess.upper()
    guessed_letters = []

    while not is_word_fully_guessed(word_to_guess, guessed_letters):
        print(f"Player{current_player_index + 1}, it's your turn:")
        print_partial_word(word_to_guess, guessed_letters)
        letter = get_single_letter_from_user(guessed_letters)
        if letter in word_to_guess:
            players_score[current_player_index] += word_to_guess.count(letter)
        guessed_letters.append(letter)

        current_player_index += 1
        if current_player_index == len(players_score):
            current_player_index = 0

    print("Congratulations!!! You guessed the word")
    return current_player_index


if __name__ == "__main__":
    print("Starting Game\n")

    players_score = [0, 0]
    current_player_index = 0

    words = ["system"]
    for word in words:
        current_player_index = guess_the_word_and_update_score(
            word, current_player_index, players_score
        )

    print("\nGame is over. Score:")
    for player_number, score in enumerate(players_score, 1):
        print(f"Player{player_number} : {score}")
