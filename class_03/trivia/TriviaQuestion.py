class TriviaQuestion:

    def __init__(self, question: str, answers: list[str], correct_answer_index: int):
        self._question = question
        self._answers = answers
        self._correct_index = correct_answer_index

    def ask_question(self) -> bool:

        self._print_question_and_answer()
        user_answer = self._get_answer_index_from_user()

        if user_answer == self._correct_index:
            return True
        return False

    def _print_question_and_answer(self):
        res = f"Question: {self._question}\n"
        res += "Answers:\n"
        for ord, answer in enumerate(self._answers, 1):
            res += f"{ord}. {answer}\n"

        print(res)

    def _get_answer_index_from_user(self):
        while True:
            user_input = input("What answer do you choose? ")

            if not user_input.isdigit():
                print("Bad input. Please provide a number")
                continue

            user_input_int = int(user_input)
            max_input_value = len(self._answers)
            if user_input_int < 1 or user_input_int > max_input_value:
                print(
                    f"Please provide a number between 1 and {max_input_value} (inclusive)"
                )
                continue

            return user_input_int - 1  # back to 0-based