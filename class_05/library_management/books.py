from pydantic import BaseModel





class Book(BaseModel):
    identifier: str

    title: str
    author: str
    isbn: str
    pages: int
    description: str




