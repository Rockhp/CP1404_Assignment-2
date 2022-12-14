"""
Replace the contents of this module docstring with your own details
Name:
Date started:
GitHub URL:
"""

# Copy your first assignment to this file, then update it to use Book class
# Optionally, you may also use BookCollection class

from book import Book
from bookcollection import BookCollection

def main():
    """..."""
    print("Reading Tracker 1.0 - by Your Name")
    books = BookCollection()
    books.load_books('books.csv', backup=True)
    print('{} books loaded'.format(len(books)))

    while True:
        choice = input("Menu:\nL - List all books\nA - Add new book\n"
                       "M - Mark a book as completed\nQ - Quit\n").lower()

        if choice not in ["l", "a", "m", "q"]:
            print("Invalid menu choice")

        if choice == "q":
            print('{} books saved to books.csv'.format(len(books)))
            print("So many books, so little time. Frank Zappa")
            break

        if choice == "l":
            print(books)

        if choice == "a":
            books.add_book(Book(*get_added_book()))

        if choice == "m":
            edit_entry(books)

# def list_all_books():
#     pages_to_read = 0
#     books_to_read = 0

#     with open('books.csv', 'r') as booklist:
#         books = booklist.readlines()
#         for book in books:
#             idx = books.index(book)
#             book = books[idx].rstrip("\n").split(",")
#             if book[3] == 'r':
#                 print(f"*{idx+1}: {book[0]}     by {book[1]}    {book[2]} pages")
#                 pages_to_read += int(book[2])
#                 books_to_read += 1
#             else:
#                 print(f" {idx+1}: {book[0]}     by {book[1]}    {book[2]} pages")
#     print(f"You will need to read {pages_to_read} pages in {books_to_read} books")

def get_added_book():
    """Add command implementation."""
    # Create a new book and add it to the list of books
    book = [
        add_text('title'),
        add_text('author'),
        add_integer('pages'),
        'r'
    ]
    print('{0}, ({1} pages) added to {2}'.format(
        book[0],
        book[2],
        'Reading Tracker'
    ))
    return book

def add_text(name):
    """Add text entry."""
    # Add string entry and check its validity
    is_valid_input = False
    # PyCharm requirement
    entry = ''
    while not is_valid_input:
        try:
            entry = input('{}: '.format(name.capitalize())).strip()
            if not entry:
                raise ValueError('Input can not be blank')
            else:
                is_valid_input = True
        except ValueError as exc:
            print(exc)
    return entry

def add_integer(number='>>>'):
    """Add numeric entry."""
    if number != '>>>':
        number = number.capitalize() + ':'
    # Add numeric entry and check its validity
    is_valid_input = False
    # PyCharm requirement
    entry = ''
    while not is_valid_input:
        try:
            entry = input('{} '.format(number))
            try:
                # Trying to convert to int
                number = int(entry)
            except ValueError:
                raise ValueError('Invalid input; enter a valid number')
            if number <= 0:
                raise ValueError('Number must be > 0')
            else:
                is_valid_input = True
        except ValueError as exc:
            print(exc)
    return number

def edit_entry(books):
    """Mark command implementation."""
    is_input_required = is_required(books)
    # Header output if required books are available
    if is_input_required:
        print(books)
        print('Enter the number of a book to mark as completed')
    # Enter the number of the completed book
    while is_input_required:
        idx = int(add_integer()) - 1
        if idx > len(books)-1:
            print('Invalid book number')
        elif books[idx].is_completed:
            print('That book is already completed')
            break
        else:
            books[idx].mark_completed()
            print('{0} by {1} completed!'.format(
                books[idx].title,
                books[idx].author
            ))
            break
    else:
        print('No required books')


def is_required(books):
    """Detects the presence of the required books"""
    required = False
    for book in books:
        # Search books marked REQUIRED
        if not book.is_completed:
            required = True
            break
    return required


# def edit_entry():
#     status = []
#     while True:
#         with open("books.csv", 'r') as booklist:
#             file_of_books = booklist.readlines()
#             for line in file_of_books:
#                 last_char = line.strip('\n')
#                 status.append(last_char[-1])
#             print(status)
#             if "r" not in status:
#                 print("There are no required books!\n")
#                 break
#             else:
#                 list_all_books()

#         idx = input("Enter the number of a book to mark as completed\n")
#         valid = False
#         while not valid:
#             try:
#                 idx = int(idx)
#                 if idx > 0 and idx < len(file_of_books)+1:
#                     valid = True
#                     break
#                 else:
#                     if idx <= 0:
#                         print("Number must be > 0")
#                     else:
#                         print("Invalid book number")
#                     valid = False
#             except:
#                 print("Invalid input; enter a valid number")
#                 valid = False
#             if not valid:
#                 idx = input("Enter the number of a book to mark as completed\n")

#         chosen_book = file_of_books[idx-1].split(',')
#         if chosen_book[-1] == "c\n":
#             print("That book is already completed")
#             break
#         else:
#             chosen_book[-1] = "c\n"
#             book_to_write = ",".join(chosen_book)
#             file_of_books[idx-1] = book_to_write
#             book_to_print = book_to_write.rstrip("\n").split(",")
#             print(f"{book_to_print[0]}     by {book_to_print[1]}    completed")

#         with open("books.csv", "w") as booklist:
#             booklist.writelines(file_of_books)
#         break

if __name__ == '__main__':
    main()
