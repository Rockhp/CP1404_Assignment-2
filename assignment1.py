"""
Replace the contents of this module docstring with your own details
Name: Rajkumar Senthilraj Ragulraj
Date started: 20th April 2022
GitHub URL:
"""


def main():
    """..."""
    print("Reading Tracker 1.0 - by Your Name")
    with open('books.csv') as booklist:
        print(f"{len(booklist.readlines())} books loaded")

    while True:
        choice = input("Menu:\nL - List all books\nA - Add new book\n"
                       "M - Mark a book as completed\nQ - Quit\n").lower()

        if choice not in ["l", "a", "m", "q"]:
            print("Invalid menu choice")

        if choice == "q":
            with open('books.csv', 'r') as booklist:
                print(f"{len(booklist.readlines())} books saved to books.csv")
                print("So many books, so little time. Frank Zappa")
            break

        if choice == "l":
            list_all_books()

        if choice == "a":
            add_new_book()

        if choice == "m":
            edit_entry()

def list_all_books():
    pages_to_read = 0
    books_to_read = 0

    with open('books.csv', 'r') as booklist:
        books = booklist.readlines()
        for book in books:
            idx = books.index(book)
            book = books[idx].rstrip("\n").split(",")
            if book[3] == 'r':
                print(f"*{idx+1}: {book[0]}     by {book[1]}    {book[2]} pages")
                pages_to_read += int(book[2])
                books_to_read += 1
            else:
                print(f" {idx+1}: {book[0]}     by {book[1]}    {book[2]} pages")
    print(f"You will need to read {pages_to_read} pages in {books_to_read} books")

def add_new_book():
    is_valid = False
    with open('books.csv', 'a') as booklist:
        title = input("Title: ")
        while len(title) == 0:
            print("Input can not be blank")
            title = input("Title: ")

        author = input("Author: ")
        while len(author) == 0:
            print("Input can not be blank")
            author = input("Author: ")

        pages = input("Pages: ")
        valid = False
        while not valid:
            try:
                pages = int(pages)
                if pages > 0:
                    valid = True
                    break
                else:
                    print("Number must be > 0")
                    valid = False
            except:
                print("Invalid input; enter a valid number")
                valid = False
            if not valid:
                pages = input("Pages: ")

        new_book = f"{title},{author},{pages},r\n"
        booklist.writelines(new_book)
        print(f"{title} by {author}, ({pages})  added to Reading Tracker")

def edit_entry():
    status = []
    while True:
        with open("books.csv", 'r') as booklist:
            file_of_books = booklist.readlines()
            for line in file_of_books:
                last_char = line.strip('\n')
                status.append(last_char[-1])
            print(status)
            if "r" not in status:
                print("There are no required books!\n")
                break
            else:
                list_all_books()

        idx = input("Enter the number of a book to mark as completed\n")
        valid = False
        while not valid:
            try:
                idx = int(idx)
                if idx > 0 and idx < len(file_of_books)+1:
                    valid = True
                    break
                else:
                    if idx <= 0:
                        print("Number must be > 0")
                    else:
                        print("Invalid book number")
                    valid = False
            except:
                print("Invalid input; enter a valid number")
                valid = False
            if not valid:
                idx = input("Enter the number of a book to mark as completed\n")

        chosen_book = file_of_books[idx-1].split(',')
        if chosen_book[-1] == "c\n":
            print("That book is already completed")
            break
        else:
            chosen_book[-1] = "c\n"
            book_to_write = ",".join(chosen_book)
            file_of_books[idx-1] = book_to_write
            book_to_print = book_to_write.rstrip("\n").split(",")
            print(f"{book_to_print[0]}     by {book_to_print[1]}    completed")

        with open("books.csv", "w") as booklist:
            booklist.writelines(file_of_books)
        break

if __name__ == '__main__':
    main()
