def print_question(question: str, answers: list[str]):
    print(f"Question: {question}")
    for i, answer in enumerate(answers, 1):
        print(f"\t{i}. {answer}")


def get_answer_index_from_user(answers_num: int): 
    while True:
        raw_input = input("Please select an answer (number): ")
        if not raw_input.isdigit():
            print("Bad input. Please provide a positive number")
            continue
        input_number = int(raw_input)
        if input_number < 1 or input_number > answers_num:
            print(f"Bad input. Please provide numbers in range [1, {answers_num}]")
            continue

        return input_number - 1



def ask_a_question(question: str, answers: list[str], correct_index: int):

    print_question(question, answers)
    answer_index = get_answer_index_from_user(len(answers))

    if answer_index == correct_index:
        return True
    return False


if __name__ == "__main__":
    print("Starting Game")

    success = ask_a_question(
        "What is the capital of Brazil",
        ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
        2,
    )

    if success:
        print("You are correct")
    else:
        print("You are a failure")
