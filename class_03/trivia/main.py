from question import Question


if __name__ == "__main__":
    print("Starting Game")

    q1 = Question(
        "What is the capital of Brazil",
        ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
        2,
    )

    success = q1.ask_a_question()
    if success:
        print("You are correct")
    else:
        print("You failed.")
