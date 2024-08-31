
from pathlib import Path
import json
from uuid import uuid4
import json

from books import Book

ROOT_DIR = Path(__file__).parent
PERSISTENT_DATA_DIR = ROOT_DIR / "persistent_data"
SAMPLE_DATA_DIR = ROOT_DIR / "sample_data"


def load_initial_book_inventory():
    sample_books_file = SAMPLE_DATA_DIR / "books.json"
    assert sample_books_file.is_file()

    books = []
    for book_data in json.loads(sample_books_file.read_text()):
        books.append(
            Book(
                identifier=str(uuid4()),
                pages=book_data["numberOfPages"],
                **book_data,
            )
        )

    books_dicts_list = [book.model_dump() for book in books]
    
    books_file = PERSISTENT_DATA_DIR / "books.json"
    books_file.write_text(json.dumps(books_dicts_list, indent=2))



if __name__ == "__main__":

    books_file = PERSISTENT_DATA_DIR / "books.json"
    books = []
    if books_file.is_file():
        for book_dict in json.loads(books_file.read_text()):
            books.append(Book.model_validate(book_dict))
    else:
        books_file.write_text(json.dumps(books))

    print(books)

    print("So far so good")

    # load_initial_book_inventory()
