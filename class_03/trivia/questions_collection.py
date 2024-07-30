from collections import defaultdict
import random

from question import Question
from validated_question import ValidatedQuestion
from utils import get_int_input_in_range, clean_empty_keys_from_dict


class QuestionCollection:

    def __init__(self, questions: list[Question]):
        self._questions_by_category = defaultdict(list)
        for question in questions:
            self._questions_by_category[question.category].append(question)

    def __len__(self):
        values = []
        for questions in self._questions_by_category.values():
            values += questions
        return len(values)

    def is_empty(self):
        return len(self._questions_by_category.keys()) == 0

    def pop_question_by_category(self) -> Question:
        category_list = list(self._questions_by_category.keys())

        if len(category_list) > 1:
            print("These are the available categories:")
            for i, category in enumerate(category_list, 1):
                print(f"{i}. {category}")

            user_category_selection = get_int_input_in_range(
                1, len(category_list), "Please select a category (by number): "
            )
            selected_category = category_list[user_category_selection - 1]
        else:
            selected_category = category_list[0]
            print(f"Only one category left: {selected_category}")

        selected_question = self._questions_by_category[selected_category].pop(0)
        clean_empty_keys_from_dict(self._questions_by_category)

        return selected_question

    @classmethod
    def build_from_file(cls, file_path: str, max_questions: int | None = None):
        validated_questions = ValidatedQuestion.get_questions_from_file(file_path)
        game_questions = [
            QuestionCollection.game_question_from_validated_question(q)
            for q in validated_questions
        ]
        if max_questions is not None:
            game_questions = game_questions[:max_questions]
        return cls(game_questions)

    @staticmethod
    def game_question_from_validated_question(q: ValidatedQuestion):
        answers = q.incorrectAnswers + [q.correctAnswer]
        random.shuffle(answers)
        correct_index = answers.index(q.correctAnswer)

        return Question(q.question, answers, correct_index, q.difficulty, q.category)
