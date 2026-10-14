import tkinter as tk

from Controllers.auth_controller import AuthController
from Models.auth_model import AuthModel
from Models.database import Database
from Views.login_view import LoginView


def main() -> None:
	database = Database()
	auth_model = AuthModel(database)
	root = tk.Tk()
	AuthController(root, LoginView(root), auth_model)
	root.mainloop()


if __name__ == "__main__":
	main()
