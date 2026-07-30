class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed:
            print("Book not avalible.")
        else:
            self.is_borrowed = True
            print("Borrowed successfully.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print("Returned successfully.")
        else:
            print("Book not Borrowed!")

    def book_status(self):
        return self.is_borrowed

    def display_info(self):
        print("Title".ljust(6) + f": {self.title}")
        print("Author".ljust(6) + f": {self.author}")
        if self.book_status():
            print("Status".ljust(6) + ": Borrowed" + "")
        else:
            print("Status".ljust(6) + ": Available" + "")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        if self.books:
            for index, book in enumerate(self.books):
                print(f"{index + 1}.")
                book.display_info()
        else:
            print("There no books for now.")

    def borrow_book(self):
        if self.books:
            index = input("Book number: ").strip()
            try:
                index = int(index)
            except ValueError:
                print("Only numbers!")
            else:
                if 0 < index <= len(self.books):
                    self.books[index - 1].borrow()
                else:
                    print("Invalid book number!")
        else:
            print("There no books for now.")

    def return_book(self):
        if self.books:
            index = input("Book number: ").strip()
            try:
                index = int(index)
            except ValueError:
                print("Only numbers!")
            else:
                if 0 < index <= len(self.books):
                    self.books[index - 1].return_book()
                else:
                    print("Invalid book number!")
        else:
            print("There no books for now.")

    def books_count(self):
        return len(self.books)


# -------- MAIN FUNCTION --------


def main():

    library = Library()
    while True:
        print("\n" + "=" * 40)
        print("Library".center(40))
        print("=" * 40)

        print("1. Add Book")
        print("2. View Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Books Count")
        print("6. Exit")

        user_selector = input("=> ").strip()
        try:
            user_selector = int(user_selector)
        except ValueError:
            print("Only numbers!")
        else:
            # -------- ADD BOOK --------

            if user_selector == 1:
                print(" Add Book ".center(40, "-"))

                title = input("Title: ").strip()
                author = input("Author: ").strip().title()
                book = Book(title, author)
                library.add_book(book)
                print(f'"{title}" added successfully.')

            # -------- VIEW BOOKS --------

            elif user_selector == 2:
                print(" View Books ".center(40, "-"))
                library.view_books()

            # -------- BORROW BOOK --------

            elif user_selector == 3:
                print(" Borrow Book ".center(40, "-"))
                library.borrow_book()
            # -------- RETURN BOOK --------

            elif user_selector == 4:
                print(" Return Book ".center(40, "-"))
                library.return_book()
            # -------- COUNT BOOK --------

            elif user_selector == 5:
                print(" Books Count ".center(40, "-"))
                print(f"Total books = {library.books_count()}")
            # -------- EXIT --------

            elif user_selector == 6:
                print("Goodbye :)")
                break
            else:
                print("Wrong number!")


main()
