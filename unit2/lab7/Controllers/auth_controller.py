import tkinter as tk
from tkinter import messagebox

import psycopg

from Models.auth_model import AuthModel
from Views.login_view import LoginView


class AuthController:
    def __init__(self, root: tk.Tk, view: LoginView, model: AuthModel) -> None:
        self.root = root
        self.view = view
        self.model = model
        self.view.set_login_handler(self.login)
        self.view.set_register_handler(self.register)
        self.view.set_check_db_handler(self.check_database_connection)

    def check_database_connection(self) -> None:
        try:
            connected = self.model.check_database_connection()
        except psycopg.Error as error:
            messagebox.showerror("Database connection failed", str(error))
            return

        if connected:
            messagebox.showinfo("Database status", "Connection successful!")
        else:
            messagebox.showerror("Database status", "Connection failed.")

    def login(self) -> None:
        username, password = self.view.credentials()
        if not username or not password:
            messagebox.showwarning("Missing details", "Enter a username and password.")
            return

        try:
            authenticated = self.model.authenticate(username, password)
        except psycopg.Error as error:
            messagebox.showerror("Database error", str(error))
            return

        if authenticated:
            messagebox.showinfo("Login successful", f"Welcome, {username}!")
        else:
            messagebox.showerror("Login failed", "Invalid username or password.")

    def register(self) -> None:
        username, password = self.view.credentials()
        if not username or not password:
            messagebox.showwarning("Missing details", "Enter a username and password.")
            return

        try:
            created = self.model.register_user(username, password)
        except psycopg.Error as error:
            messagebox.showerror("Database error", str(error))
            return

        if created:
            messagebox.showinfo("Registration successful", "User was created successfully.")
        else:
            messagebox.showerror("Registration failed", "This username already exists or is invalid.")
