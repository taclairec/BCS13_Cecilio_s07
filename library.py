class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_publication_year(self):
        return self.publication_year

    def is_book_available(self):
        return self.is_available

    def borrow_book(self):
        self.is_available = False

    def return_book(self):
        self.is_available = True


library = []

print("")
print("WELCOME TO VERNONLINE'S ONLINE LIBRARY!")

def display_library_books():
    print("")
    print("Available books in the library:")
    for index, book in enumerate(library):
        print(f"{index + 1}. {book.get_title()} by {book.get_author()} ({book.get_publication_year()})")
        if book.is_book_available():
            print("   Status: Available")
        else:
            print("   Status: Borrowed")
    print("")

def book_details():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    publication_year = input("Enter the publication year of the book: ")
    return title, author, publication_year

def add_library(title, author, publication_year):
    book = Book(title, author, publication_year)
    library.append(book)
    print("Book added to the library successfully.")
    print("")

def borrow_book():
    display_library_books()
    index = int(input("Enter INDEX of the book you wish to BORROW: ")) - 1
    if 0 <= index < len(library):
        book = library[index]
        if book.is_book_available():
            book.borrow_book()
            print("Book borrowing SUCCESSFUL!")
        else:
            print("Book Borrowing UNSUCCESSFUL!")
    else:
        print("Invalid book index!")
    print("")

def return_book():
    display_library_books()
    index = int(input("Enter INDEX of the book you wish to RETURN: ")) - 1
    if 0 <= index < len(library):
        book = library[index]
        if not book.is_book_available():
            book.return_book()
            print("Book return SUCCESSFUL!")
        else:
            print("Book return UNSUCCESSFUL!")
    else:
        print("INVALID book index.")
    print("")

# Prompt the user to enter book details

while True:
    print("")
    option = input("'A' - add a book | 'B' - borrow a book | 'R' - return a book | or 'X' - quit: ")
    if option.upper() == 'A':
        title, author, publication_year = book_details()
        add_library(title, author, publication_year)
    elif option.upper() == 'B':
        borrow_book()
    elif option.upper() == 'R':
        return_book()
    elif option.upper() == 'X':
        break
    else:
        print("Invalid choice. Please try again.")

display_library_books()
print("")
print("Thank you for visiting VERNONLINE's Online Bookstore!")
