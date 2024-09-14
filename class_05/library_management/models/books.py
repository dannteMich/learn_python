from pydantic import BaseModel

from interfaces import TextSearchable

class Book(BaseModel, TextSearchable):
    identifier: str

    title: str
    author: str
    isbn: str
    pages: int
    description: str

    def get_searchable_text(self) -> str:
        return f"{self.title} {self.author} {self.description}"
