# POLYMORPHISM

import tkinter as tk
from abc import ABC, abstractmethod
from pathlib import Path
from tkinter import ttk


class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

    # Abstract method forced every child class to create its own turn_on method
    # If a child gets created without a turn_on() method, it will raise an error
    # Provides its unique implementation

    @abstractmethod
    def turn_on(self):
        pass


class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living Room Light")

    def turn_on(self):
        return f"{self.name} set the brightness to 70%"


class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Room 01 Speaker")

    def turn_on(self):
        return f"{self.name} is now ready to play music"


class SmartFridge(SmartDevice):
    def __init__(self):
        super().__init__("Smart Fridge Model X")

    def turn_on(self):
        return f"{self.name} is now operating at optimal temperature"


class SmartThermostat(SmartDevice):
    def __init__(self):
        super().__init__("Smart Thermostat")

    def turn_on(self):
        return f"{self.name} is set to 22 degrees Celsius"


# GUI with tkinter
class PolymorphicAppTemplate(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- 1. WINDOW SETTINGS---
        self.title("OOP Lab: Polymorphism GUI Template")
        self.geometry("480x360")
        self.resizable(True, True)
        self.dark_mode = False
        self.colors = {
            "light": {
                "background": "#f4f4f4",
                "surface": "#ffffff",
                "text": "#111111",
                "muted": "#555555",
                "border": "#d2d2d2",
                "button": "#111111",
                "button_text": "#ffffff",
                "output": "#e9e9e9",
            },
            "dark": {
                "background": "#111111",
                "surface": "#1f1f1f",
                "text": "#ffffff",
                "muted": "#c7c7c7",
                "border": "#444444",
                "button": "#ffffff",
                "button_text": "#111111",
                "output": "#2b2b2b",
            },
        }

        icon_path = Path(__file__).with_name("1016562.png")
        self.icon_source = tk.PhotoImage(file=icon_path)
        self.window_icon = self.icon_source.subsample(16, 16)
        self.iconphoto(True, self.window_icon)

        # --- 2. OBJECT REGISTRY---
        # Map a friendly Radiobutton label to an instantiated object:
        self.items = {
            "Smart Speaker": SmartSpeaker(),
            "Smart Fridge": SmartFridge(),
            "Smart Light": SmartLight(),
            "Smart Thermostat": SmartThermostat(),
        }

        # Build visual components
        self._build_interface()

    def _build_interface(self):
        # Header / Title Banner
        self.lbl_header = tk.Label(
            self, text="POLYMORPHISM", font=("DejaVu Sans", 22, "bold")
        )
        self.lbl_header.pack(pady=12)

        # Selection Group (Radiobuttons)
        self.group_box = tk.LabelFrame(
            self,
            text=" Select an Option ",
            font=("DejaVu Sans", 12, "bold"),
            padx=15,
            pady=10,
        )
        self.group_box.pack(fill="x", padx=20, pady=5)

        # Default selection: first key in dictionary
        first_key = next(iter(self.items))
        self.selected_key = tk.StringVar(value=first_key)

        # Automatically generates a radiobutton for each item in self.items
        for key in self.items:
            rb = ttk.Radiobutton(
                self.group_box,
                text=key,
                value=key,
                variable=self.selected_key,
                style="Mono.TRadiobutton",
            )
            rb.pack(anchor="w", pady=3)

        self.controls = tk.Frame(self)
        self.controls.pack(pady=15)

        # Trigger Action Button
        self.btn_action = tk.Button(
            self.controls,
            text="EXECUTE ACTION",
            command=self._handle_action,
            font=("DejaVu Sans", 11, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=6,
        )
        self.btn_action.pack(side="left", padx=5)

        self.theme_button = tk.Button(
            self.controls,
            text="DARK MODE",
            command=self._toggle_theme,
            font=("DejaVu Sans", 11, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=6,
        )
        self.theme_button.pack(side="left", padx=5)

        # Output / Results Box
        self.lbl_output = tk.Label(
            self,
            text="Select an option above and click 'EXECUTE ACTION'.",
            font=("DejaVu Sans", 12, "italic"),
            relief="flat",
            height=3,
            wraplength=420,
            justify="center",
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)
        self._apply_theme()

    def _apply_theme(self):
        theme_name = "dark" if self.dark_mode else "light"
        colors = self.colors[theme_name]

        self.configure(bg=colors["background"])
        self.controls.configure(bg=colors["background"])
        self.lbl_header.configure(bg=colors["background"], fg=colors["text"])
        self.group_box.configure(
            bg=colors["surface"],
            fg=colors["text"],
            highlightbackground=colors["border"],
        )
        self.btn_action.configure(
            bg=colors["button"],
            fg=colors["button_text"],
            activebackground=colors["text"],
            activeforeground=colors["button_text"],
        )
        self.theme_button.configure(
            text="LIGHT MODE" if self.dark_mode else "DARK MODE",
            bg=colors["surface"],
            fg=colors["text"],
            activebackground=colors["output"],
            activeforeground=colors["text"],
            highlightbackground=colors["border"],
        )
        self.lbl_output.configure(
            bg=colors["output"],
            fg=colors["muted"],
        )

        ttk.Style().configure(
            "Mono.TRadiobutton",
            background=colors["surface"],
            foreground=colors["text"],
            font=("DejaVu Sans", 11),
        )

    def _toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self._apply_theme()

    def _handle_action(self):
        # 1. Get the current key selected by the user
        chosen_key = self.selected_key.get()

        # 2. Retrieve the active polymorphic object
        active_object: SmartDevice = self.items[chosen_key]

        # 3. POLYMORPHIC EXECUTION:
        # No 'if/elif' logic needed. Python runs the appropriate implementation!
        result_message = active_object.turn_on()

        # 4. Display result in the UI
        self.lbl_output.config(text=result_message, font=("DejaVu Sans", 12, "normal"))


# =====================================================================
# LAUNCHER
# =====================================================================
if __name__ == "__main__":
    app = PolymorphicAppTemplate()
    app.mainloop()
