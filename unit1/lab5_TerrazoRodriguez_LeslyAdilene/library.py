class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_users(self, user):
        self.users.append(user)

    def show_books(self):
        for book in self.books:
            print(book.show_books())

    def show_users(self):
        for user in self.users:
            print(user.show_users())

    def find_book(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book

        return None

    def find_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user

        return None
