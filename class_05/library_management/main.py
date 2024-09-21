from uuid import uuid4
from pick import pick

from models.books import Book
from models.readers import Reader
import business_logic as bl

BOOKS = "books"
READERS = "readers"

ADD = "add"
QUERY = "query"

QUERY_TYPE_TITLE = "title"
QUERY_TYPE_AUTHOR = "author"
QUERY_TYPE_TEXT = "free text"


def raise_unknown_options():
    raise RuntimeError("Unknown Option")


def is_valid_isbn(isbn: str):
    clean_isbn = isbn.replace("-", "")
    return clean_isbn.isdigit() and len(clean_isbn) == 10


def add_book_from_user() -> Book:
    title = input("Title of the book: ").strip()
    author = input("Books' author:").strip()
    isbn = input("Book's ISBN code: ").strip()
    while not is_valid_isbn(isbn):
        isbn = input("Invalid ISBN code. Please try again: ").strip()
    description = input("Books' description: ").strip()
    pages = input("Book's number of pages: ").strip()
    while not pages.isdigit():
        pages = input("Invalid num of pages. try again: ").strip()
    pages = int(pages)

    new_book = Book(
        identifier=str(uuid4()),
        title=title,
        author=author,
        isbn=isbn,
        description=description,
        pages=pages,
    )
    bl.add_book(new_book)


def add_reader_from_user() -> Reader:
    name = input("Reader's name: ").strip()
    id = input("Readers id: ").strip()
    while not (len(id) == 9 and id.isdigit()):
        id = input("ID should be 9 digits. Readers id: ")
    bl.add_reader(Reader(name=name, identifier=id))


def handle_books():
    choice, _ = pick([ADD, QUERY], "What do you want to do with the books?")
    if choice == ADD:
        add_book_from_user()
    elif choice == QUERY:
        query_type, _ = pick(
            [QUERY_TYPE_TITLE, QUERY_TYPE_AUTHOR, QUERY_TYPE_TEXT],
            "What kind of query?",
        )
        query_string = input("Please type the query string: ").strip()

        if query_type == QUERY_TYPE_TITLE:
            print(bl.books_query_by_title(query_string))
        elif query_type == QUERY_TYPE_AUTHOR:
            print(bl.books_query_by_author(query_string))
        elif query_type == QUERY_TYPE_TEXT:
            print(bl.books_query_by_free_text(query_string))
        else:
            raise_unknown_options()
    else:
        raise_unknown_options()


def handle_readers():
    choice, _ = pick([ADD, QUERY], "What do you want to do with the readers?")
    if choice == ADD:
        add_reader_from_user()
    elif choice == QUERY:
        query_string = input("Please type the part of the reader's name: ").strip()
        for reader in bl.all_readers():
            if query_string.lower() in reader.name.lower():
                print(f"{reader.identifier} - {reader.name}")
    else:
        raise_unknown_options()


if __name__ == "__main__":

    choice, _ = pick([BOOKS, READERS], "What do you want to handle?")

    if choice == BOOKS:
        handle_books()
    elif choice == READERS:
        handle_readers()
    else:
        raise_unknown_options()
