import json
from pathlib import Path

from dal.dal_utils import parse_models_from_file
from dal.FileDALSingleton import FileDALSingleton
from dal.DAL import Dal
from models.books import Book
from consts import PERSISTENT_DATA_DIR


PERSISTENT_BOOKS_DATA = PERSISTENT_DATA_DIR / "books_data.json"


class BooksInventory(FileDALSingleton, Dal):

    def __init__(self, data_file: Path = PERSISTENT_BOOKS_DATA):
        BooksInventory.initialize_class(data_file, default_file_content="[]")
        self.get_all()

    def get_all(self) -> list[Book]:
        return parse_models_from_file(self._data_file_path, Book)

    def add(self, new_book: Book):
        books = self.get_all()

        existing_identifiers = [book.identifier for book in books]
        if new_book.identifier in existing_identifiers:
            raise ValueError(f"Identifier {new_book.identifier} already exists")

        books.append(new_book)
        book_dicts = [b.model_dump() for b in books]
        self._data_file_path.write_text(json.dumps(book_dicts, indent=2))
