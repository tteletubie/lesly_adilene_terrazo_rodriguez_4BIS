import tkinter as tk
from collections.abc import Callable


class LoginView:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Chacon Login")
        self.root.geometry("430x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f3f6fb")

        self.container = tk.Frame(root, padx=30, pady=28, bg="#f3f6fb")
        self.container.pack(fill="both", expand=True)

        self.card = tk.Frame(self.container, bg="#ffffff", padx=24, pady=24)
        self.card.pack(fill="both", expand=True)

        title = tk.Label(
            self.card,
            text="Welcome back",
            font=("Segoe UI", 22, "bold"),
            fg="#1f2937",
            bg="#ffffff",
        )
        title.pack(anchor="w", pady=(0, 20))

        subtitle = tk.Label(
            self.card,
            text="Sign in to continue",
            font=("Segoe UI", 10),
            fg="#6b7280",
            bg="#ffffff",
        )
        subtitle.pack(anchor="w", pady=(0, 18))

        tk.Label(self.card, text="Username", font=("Segoe UI", 10, "bold"), fg="#374151", bg="#ffffff").pack(anchor="w")
        self.username_entry = tk.Entry(
            self.card,
            width=30,
            font=("Segoe UI", 11),
            bd=0,
            highlightthickness=1,
            highlightbackground="#d1d5db",
            highlightcolor="#3b82f6",
            bg="#f9fafb",
        )
        self.username_entry.pack(fill="x", pady=(6, 14))

        tk.Label(self.card, text="Password", font=("Segoe UI", 10, "bold"), fg="#374151", bg="#ffffff").pack(anchor="w")
        self.password_entry = tk.Entry(
            self.card,
            width=30,
            show="*",
            font=("Segoe UI", 11),
            bd=0,
            highlightthickness=1,
            highlightbackground="#d1d5db",
            highlightcolor="#3b82f6",
            bg="#f9fafb",
        )
        self.password_entry.pack(fill="x", pady=(6, 18))

        self.login_button = tk.Button(
            self.card,
            text="Log in",
            font=("Segoe UI", 10, "bold"),
            bg="#3b82f6",
            fg="#ffffff",
            relief="flat",
            padx=18,
            pady=10,
            cursor="hand2",
        )
        self.login_button.pack(fill="x", pady=(0, 10))

        self.register_button = tk.Button(
            self.card,
            text="Register",
            font=("Segoe UI", 10, "bold"),
            bg="#e2e8f0",
            fg="#0f172a",
            relief="flat",
            padx=18,
            pady=10,
            cursor="hand2",
        )
        self.register_button.pack(fill="x", pady=(0, 10))

        self.check_db_button = tk.Button(
            self.card,
            text="Check DB Connection",
            font=("Segoe UI", 10, "bold"),
            bg="#10b981",
            fg="#ffffff",
            relief="flat",
            padx=18,
            pady=10,
            cursor="hand2",
        )
        self.check_db_button.pack(fill="x")

    def set_login_handler(self, handler: Callable[[], None]) -> None:
        self.login_button.configure(command=handler)
        self.password_entry.bind("<Return>", lambda _event: handler())

    def set_register_handler(self, handler: Callable[[], None]) -> None:
        self.register_button.configure(command=handler)

    def set_check_db_handler(self, handler: Callable[[], None]) -> None:
        self.check_db_button.configure(command=handler)

    def credentials(self) -> tuple[str, str]:
        return self.username_entry.get().strip(), self.password_entry.get()
