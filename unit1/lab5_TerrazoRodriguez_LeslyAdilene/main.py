from books import Book
from users import User
from library import Library


library = Library()


while True:
    print("\033c")

    print("---- Library Management System ----\n")

    print("1.- Register a book")
    print("2.- Register a user")
    print("3.- Borrow a book")
    print("4.- Return a book")
    print("5.- Show registered users")
    print("6.- Exit")

    choice = input("Enter your choice (1-6): ")

    match choice:
        case "1":
            print("\033c")

            loop = "y"

            while loop == "y":
                book_id = input("Enter the id: ")
                name = input("Enter the name: ")
                author = input("Enter the author: ")
                publisher = input("Enter the publisher: ")

                new_book = Book(book_id, name, author, publisher)

                library.add_book(new_book)

                print(f"Book '{name}' by {author} has been registered successfully.\n")

                loop = input("Do you want to register another book? (y/n): ").lower()

        case "2":
            print("\033c")

            loop = "y"

            while loop == "y":
                user_id = input("Enter the user id: ")
                user_name = input("Enter the user name: ")

                new_user = User(user_id, user_name)

                library.add_users(new_user)

                print(f"User {user_name} has been registered successfully.\n")

                loop = input("Do you want to register another user? (y/n): ").lower()

        case "3":
            print("\033c")

            if not library.books:
                print("There are no registered books.")
                input("\nPress Enter to continue...")
                continue

            if not library.users:
                print("There are no registered users.")
                input("\nPress Enter to continue...")
                continue

            print("Registered books:\n")
            library.show_books()

            print("\nRegistered users:\n")
            library.show_users()

            print()

            user_id = input("Enter the id of the user who wants to borrow a book: ")

            book_id = input("Enter the id of the book to borrow: ")

            user = library.find_user(user_id)
            book = library.find_book(book_id)

            if user is None:
                print(f"\nUser with id '{user_id}' was not found.")

            elif book is None:
                print(f"\nBook with id '{book_id}' was not found.")

            else:
                user.borrow_book(book)

            input("\nPress Enter to continue...")

        case "4":
            print("\033c")

            if not library.books:
                print("There are no registered books.")
                input("\nPress Enter to continue...")
                continue

            print("Registered books:\n")
            library.show_books()

            print()

            user_id = input("Enter the id of the user returning the book: ")

            book_id = input("Enter the id of the book to return: ")

            user = library.find_user(user_id)
            book = library.find_book(book_id)

            if user is None:
                print(f"\nUser with id '{user_id}' was not found.")

            elif book is None:
                print(f"\nBook with id '{book_id}' was not found.")

            else:
                user.return_book(book)

            input("\nPress Enter to continue...")

        case "5":
            print("\033c")

            print("Registered users:\n")

            if not library.users:
                print("There are no registered users.")
            else:
                library.show_users()

            input("\nPress Enter to continue...")

        case "6":
            print("Exiting the program...")
            break

        case _:
            print("Invalid option.")
            input("\nPress Enter to continue...")
