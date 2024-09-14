from booksInventory import BooksInventory
from books import Book


books_inventory = BooksInventory()


def add_book(new_book: Book):
    books_inventory.add(new_book)


def all_books():
    return books_inventory.get_all()


def _books_query_by_field(field_name: str, field_value: str) -> list[Book]:
    relevant_books = []
    for book in books_inventory.get_all():
        if field_value.lower() in getattr(book, field_name).lower():
            relevant_books.append(book)

    return relevant_books


def books_query_by_author(author_query: str):
    return _books_query_by_field("author", author_query)


def books_query_by_title(title_query: str):
    return _books_query_by_field("title", title_query)

def book_by_identifier(query_identifier: str):
    for book in books_inventory.get_all():
        if book.identifier == query_identifier:
            return book
    
    return None
    
def books_query_by_free_text(text_query: str):
    relevant_books = []
    for book in books_inventory.get_all():
        if text_query.lower() in book.get_searchable_text().lower():
            relevant_books.append(book)

    return relevant_books