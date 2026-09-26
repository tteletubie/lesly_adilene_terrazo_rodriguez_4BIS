class User:
    def __init__(self, id_user, name):
        self.id = id_user
        self.name = name
        self.borrowed_books = []

    def show_users(self):
        return f"{self.id} - {self.name}"

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)

            print(f"{self.name} has borrowed the book '{book.name}'.")
        else:
            print(f"Sorry, the book '{book.name}' is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)

            print(f"{self.name} has returned the book '{book.name}'.")
        else:
            print(f"{self.name} did not borrow the book '{book.name}'.")
