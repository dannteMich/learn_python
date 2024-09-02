import json
from pathlib import Path

from books import Book

ROOT_DIR = Path(__file__).parent
PERSISTENT_DATA_DIR = ROOT_DIR / "persistent_data"
PERSISTENT_BOOKS_DATA = (
    PERSISTENT_DATA_DIR / "books_data.json"
)  # TODO: maybe should allow to change


class BooksInventory:
    instance_exists = False

    def __init__(self, data_file: Path=PERSISTENT_BOOKS_DATA):
        if BooksInventory.instance_exists:
            raise TypeError("Cannot create more than one instance of this class")
        
        self._data_file_path = data_file
        if not self._data_file_path.is_file():
            self._data_file_path.write_text("[]")

        self.get_all()
        BooksInventory.instance_exists = True

    def get_all(self) -> list[Book]:
        book_dicts = json.loads(self._data_file_path.read_text())
        books = [Book.model_validate(book_dict) for book_dict in book_dicts]

        return books

    def add(self, new_book: Book):
        books = self.get_all()
        
        existing_identifiers = [book.identifier for book in books]
        if new_book.identifier in existing_identifiers:
            raise ValueError(f"Identifier {new_book.identifier} already exists")
        
        books.append(new_book)
        book_dicts = [b.model_dump() for b in books]
        self._data_file_path.write_text(json.dumps(book_dicts, indent=2))
