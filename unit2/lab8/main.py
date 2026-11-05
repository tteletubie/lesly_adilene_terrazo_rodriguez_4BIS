import tkinter as tk

from models.login_model import UserModel
from views.login_view import LoginView
from controllers.authentication import Authentication


class System:

    def __init__(self):
        self.root = tk.Tk()

        modelo = UserModel()
        vista = LoginView(self.root)
        Authentication(modelo, vista)

    def iniciar(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = System()
    app.iniciar()