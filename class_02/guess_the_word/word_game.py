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


def guess_the_word_and_update_players(target: dict, players: list[tuple]):
    word_to_guess = target["word"]
    word_to_guess = word_to_guess.upper()
    description = target["description"]
    guessed_letters = []

    print(f"Clue: {description}")

    while not is_word_fully_guessed(word_to_guess, guessed_letters):
        player_name, player_score = players.pop(0)
        print(f"{player_name}, it's your turn:")

        print_partial_word(word_to_guess, guessed_letters)
        letter = get_single_letter_from_user(guessed_letters)
        if letter in word_to_guess:
            player_score += word_to_guess.count(letter)

        guessed_letters.append(letter)

        players.append((player_name, player_score))

    print(f"Congratulations!!! You guessed the word {word_to_guess}\n\n")
