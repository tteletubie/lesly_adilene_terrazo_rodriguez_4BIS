class Book:
    def __init__(self, id_book, name, author, editorial):
        self.id = id_book
        self.name = name
        self.author = author
        self.editorial = editorial
        self.available = True

    def show_books(self):
        status = "Available" if self.available else "Borrowed"

        return f"{self.id} - {self.name} - {self.author} - {self.editorial} - {status}"
