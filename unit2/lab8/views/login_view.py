import tkinter as tk
from tkinter import messagebox

class LoginView:

    def __init__(self, root):

        self.root = root
        self.root.title("Sistema de acceso")

  
        self.root.geometry("420x350")

        self.root.configure(bg="#EAF2F8")

        self.root.resizable(False, False)

        self.titulo = tk.Label(
            root,
            text="INICIAR SESIÓN",
            font=("Arial", 20, "bold"),
            bg="#EAF2F8",
            fg="#154360"
        )
        self.titulo.pack(pady=20)


        self.lbl_email = tk.Label(
            root,
            text="Correo electrónico:",
            font=("Arial", 11),
            bg="#EAF2F8"
        )
        self.lbl_email.pack()

       
        self.entry_email = tk.Entry(
            root,
            width=35,
            font=("Arial", 11)
        )
        self.entry_email.pack(pady=5)

        self.lbl_password = tk.Label(
            root,
            text="Contraseña:",
            font=("Arial", 11),
            bg="#EAF2F8"
        )
        self.lbl_password.pack()

        
        self.entry_password = tk.Entry(
            root,
            width=35,
            font=("Arial", 11),
            show="*"
        )
        self.entry_password.pack(pady=5)

    
        self.btn_login = tk.Button(
            root,
            text="Ingresar",
            width=20,
            bg="#2874A6",
            fg="white",
            font=("Arial", 11, "bold"),
            cursor="hand2"
        )
        self.btn_login.pack(pady=15)

        
        self.btn_register = tk.Button(
            root,
            text="Crear cuenta",
            width=20,
            bg="#27AE60",
            fg="white",
            font=("Arial", 10),
            cursor="hand2"
        )
        self.btn_register.pack()

    def obtener_datos(self):
        email = self.entry_email.get().strip()
        password = self.entry_password.get()

        return email, password

    def limpiar_campos(self):
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.root)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.root)