from pydantic import BaseModel


class ValidatedQuestion(BaseModel):
    question: str
    correctAnswer: str
    incorrectAnswers: list[str]
    category: str
    difficulty: int
    