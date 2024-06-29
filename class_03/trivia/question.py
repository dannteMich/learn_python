

class Question:

    def __init__(self, question: str, answers: list[str], correct_index: int):
        self._question = question
        self._answers = answers
        self._correct_index = correct_index

    def print_question(self):
        print(f"Question: {self._question}")
        for i, answer in enumerate(self._answers, 1):
            print(f"\t{i}. {answer}")

    def __repr__(self):
        return f"Questions {self._question}"
    
    def ask_a_question(self):
        self.print_question()
        answer_index = self._get_answer_index_from_user()

        if answer_index == self._correct_index:
            return True
        return False

    def _get_answer_index_from_user(self):
        answers_num = len(self._answers)

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
