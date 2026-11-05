import tkinter as tk
from tkinter import messagebox


def __init__(self, root):
        self.ventana.title("Registro de usuarios")        
        self.ventana.geometry("420x440")
        self.ventana.configure(bg="#E8F8F5")
        self.ventana.resizable(False, False)
        self.ventana.transient(root)
        self.ventana.grab_set()

        self.titulo = tk.Label(
            self.ventana,
            text="CREAR CUENTA",
            font=("Arial", 19, "bold"),
            bg="#E8F8F5",
            fg="#117864"
        )
        self.titulo.pack(pady=18)

        self.lbl_nombre = tk.Label(
            self.ventana,
            text="Nombre completo:",
            bg="#E8F8F5",
            font=("Arial", 10)
        )
        self.lbl_nombre.pack()

        self.entry_nombre = tk.Entry(
            self.ventana,
            width=35,
            font=("Arial", 10)
        )
        self.entry_nombre.pack(pady=4)

        self.lbl_email = tk.Label(
            self.ventana,
            text="Correo electrónico:",
            bg="#E8F8F5",
            font=("Arial", 10)
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(
            self.ventana,
            width=35,
            font=("Arial", 10)
        )
        self.entry_email.pack(pady=4)

        self.lbl_password = tk.Label(
            self.ventana,
            text="Contraseña:",
            bg="#E8F8F5",
            font=("Arial", 10)
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            self.ventana,
            width=35,
            show="*",
            font=("Arial", 10)
        )
        self.entry_password.pack(pady=4)

        self.lbl_confirmar = tk.Label(
            self.ventana,
            text="Confirmar contraseña:",
            bg="#E8F8F5",
            font=("Arial", 10)
        )
        self.lbl_confirmar.pack()

        self.entry_confirmar = tk.Entry(
            self.ventana,
            width=35,
            show="*",
            font=("Arial", 10)
        )
        self.entry_confirmar.pack(pady=4)

        self.btn_guardar = tk.Button(
            self.ventana,
            text="Registrar usuario",
            width=22,
            bg="#17A589",
            fg="white",
            font=("Arial", 10, "bold"),
            cursor="hand2"
        )
        self.btn_guardar.pack(pady=12)

        self.btn_cancelar = tk.Button(
            self.ventana,
            text="Cancelar",
            width=22,
            command=self.cerrar,
            cursor="hand2"
        )
        self.btn_cancelar.pack()

        self.entry_nombre.focus_set()

def obtener_datos(self):
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get()
        confirmar = self.entry_confirmar.get()

        return nombre, email, password, confirmar

def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(
                titulo,
                mensaje,
                parent=self.ventana
            )
        else:
            messagebox.showinfo(
                titulo,
                mensaje,
                parent=self.ventana
            )

def cerrar(self):
    self.ventana.destroy()


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