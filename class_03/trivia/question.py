from utils import get_int_input_in_range


class Question:

    def __init__(
        self,
        question: str,
        answers: list[str],
        correct_index: int,
        difficulty: int,
        category: str,
    ):
        self._question = question
        self._answers = answers
        self._correct_index = correct_index
        self._difficulty = difficulty
        self._category = category

    @property
    def category(self):
        return self._category

    @property
    def difficulty(self):
        return self._difficulty

    def print_question(self):
        print(f"Question with difficulty {self._difficulty}: {self._question}")
        for i, answer in enumerate(self._answers, 1):
            print(f"\t{i}. {answer}")

    def __repr__(self):
        return f"Questions {self._question}"

    def ask_a_question(self) -> bool:
        """Asks the user the question. Return True if he answers correctly"""
        self.print_question()
        answer_index = self._get_answer_index_from_user()

        if answer_index == self._correct_index:
            return True
        return False

    def _get_answer_index_from_user(self):
        answers_num = len(self._answers)
        user_choice = get_int_input_in_range(
            1, answers_num, "Please select an answer (number): "
        )

        return user_choice - 1
