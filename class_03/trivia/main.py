from TriviaQuestion import TriviaQuestion


if __name__ == "__main__":
    print("starting game")

    first_question = TriviaQuestion(
        "What is the capital of Brazil?",
        ["Buenos Aires", "São Paulo", "Rio de Janeiro", "Brasília"],
        3,
    )

    success = first_question.ask_question()
    if success:
        print("You are correct")
    else:
        print("YOu are a failure")
