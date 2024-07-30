import json
import pathlib
import random

from pydantic import BaseModel


class ValidatedQuestion(BaseModel):
    question: str
    correctAnswer: str
    incorrectAnswers: list[str]
    category: str
    difficulty: int
    
    @staticmethod
    def get_questions_from_file(file_path: str):
        questions_file = pathlib.Path(file_path)
        assert questions_file.exists(), "File does not exist"
        questions_list = json.load(questions_file.open())

        game_questions = [ValidatedQuestion.model_validate(q) for q in questions_list]
        random.shuffle(game_questions)
        return game_questions