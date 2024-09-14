from uuid import uuid4
from pick import pick

from books import Book
import business_logic as books_actions

ADD = "add"
QUERY = "query"

QUERY_TYPE_TITLE = "title"
QUERY_TYPE_AUTHOR = "author"
QUERY_TYPE_TEXT = "free text"


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
    books_actions.add_book(new_book)


if __name__ == "__main__":

    choice, _ = pick([ADD, QUERY], "What do you want to do with the books?")
    if choice == ADD:
        add_book_from_user()
    elif choice == QUERY:
        query_type, _ = pick([QUERY_TYPE_TITLE, QUERY_TYPE_AUTHOR, QUERY_TYPE_TEXT], "What kind of query?")
        query_string = input("Please type the query string: ").strip()
        
        if query_type == QUERY_TYPE_TITLE:
            print(books_actions.books_query_by_title(query_string))
        elif query_type == QUERY_TYPE_AUTHOR:
            print(books_actions.books_query_by_author(query_string))
        elif query_type == QUERY_TYPE_TEXT:
            print(books_actions.books_query_by_free_text(query_string))