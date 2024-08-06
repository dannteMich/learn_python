## Knowledge required
In addition to the previous classes, the following additional knowledge is required:

- inheritance
- Exceptions

### packages required:
most of the packages required for this exercise are built in and used in previous exercises. `pydantic` can be used (but not necessary).

You might want to use `typer` as a replacement for `argparse`

## The Exercise

This exercise is a bit complicated, but it's important you understand the requirement correctly, as this exercise will form the base and foundation for exercise 6.

### Core functionality

### Additional information and requirements

### Required Actions and and Queries

- Types of items to rent
  - Book
    - Title
    - Author
    - ISBN
    - Pages
    - Back Text
  - Magazine
    - Name
    - Publishing Date
    - List of articles. For each article:
      - Title
      - Author
  - DVD
    - Title
    - Director
    - Actors
    - Duration
    - Date released
    - Back text
  

- Actions
  - Add a book to the library
  - Add a magazine to the library
  - Add a DVD to the library
  - Register a "reader" to the library
  - Borrow an item by a reader
- Queries
  - All books by an author
  - All magazines from a period time
  - All Movies by some Director
  - All Movies with some actor
  - Search by Title
  - Free text search - all items with a substring in their "info"
  - All borrowed items by a given reader
  - All borrowed books by a given reader
  - All borrowed magazines by a given reader
  - All "late" readers - readers that have an over-due borrowed item
  - 