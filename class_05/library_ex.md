## Knowledge required
In addition to the previous classes, the following additional knowledge is required:

- inheritance

### packages required:
most of the packages required for this exercise are built in and used in previous exercises. `pydantic` can be used (but not necessary).

You might want to use `typer` as a replacement for `argparse`

## The Exercise

This exercise is a bit complicated, but it's important you understand the requirement correctly, as this exercise will form the base and foundation for exercise 6.

In this exercise, you will implement a library system. This library will have registered readers, that can borrow various items from the libraries inventory.

You will have to deal with registering new readers and new items, borrowing and returning items, and also quiring data.

Also, all of this should be "shut-down" safe, meaning that if the program is stopped and started again, all the data should be saved and restored.

### Core functionality

The library system will have the following features:

- The library has a collection of items that can be borrowed by readers:
  - Books - can be borrowed for 30 days
  - Magazines - can be borrowed for 7 days
  - DVDs (movies) can be borrowed for 14 days
- Each of these items has different properties, and the library should be able to store all of them. Please see the [Types of items to borrow](#types-of-items-to-borrow) section for more details.
- For the sake of simplicity, assume that there is only 1 copy of each item.
- **Readers** can borrow items from the library. if they are available. Each reader can borrow up to 3 items at a time.
- You need to allow the registration of new readers to the library, as well as the addition of new items to the library.



A list of all the actions and queries required can be found in the [Required Actions](#required-actions) and [Required Queries](#required-queries) sections.


It's important to note that once an action is complete, the new state of the system should be "restart-tolerant", meaning that if the program is stopped and started again (or the computer crushes and is restarted), the new state should be restored when the program is started again.

The easiest way to do this is to save the state of the system to a file, and then load it when the program starts. You choose what files and what format.

#### How the user interacts with the program

The user should interact with the program using the command line. The program should be able to accept commands and queries from the user, and return the results to the user.

This can be done in (at least) two ways:
1. Inside the program - the program starts, and then accepts an input from the user that will provide the action\query and all it's parameters. The program will then execute the action\query and return the result to the user, and then again wait for the next input.
2. From outside the program - When the user starts the program, he provides the action\query and all it's parameters as command-line arguments. The program will then execute the action\query and return the result to the user, and then exit.

Both ways are acceptable. You can choose the one that you think is more suitable for you.


### Additional information, requirements, and details



#### Types of items to borrow

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
  - Description
  
You are welcome to add more properties to each item if you think it's needed (like id, catalog number, etc.).

Files with sample data for each item type are provided with the exercise.

#### Required Actions 
- Register a "reader" to the library
- Add a book to the library
- Add a magazine to the library
- Add a DVD to the library
- Borrow an item by a reader

#### Required Queries


- All books by an author
- All magazines from a period time
- All Movies by some Director
- All Movies with some actor
- Search by Title
- Free text search - all items with a substring in their "info"
- All borrowed items by a given reader
- All borrowed books by a given reader
- All borrowed magazines by a given reader
- All "late" items - items that are borrowed and not returned on time
- All "late" readers - readers that have an over-due borrowed item