from uuid import uuid4
from pathlib import Path

from booksInventory import BooksInventory
from books import Book


if __name__ == "__main__":

    books_inventory = BooksInventory()
    print(books_inventory.get_all())
    books_inventory = BooksInventory()

    

    print("So far so good")
