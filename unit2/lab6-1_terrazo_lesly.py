# POLYMORPHISM

import tkinter as tk
from abc import ABC, abstractmethod
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

    @abstractmethod
    def turn_off(self):
        pass


class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living Room Light")

    def turn_on(self):
        return f"{self.name} set the brightness to 70%"

    def turn_off(self):
        return f"{self.name} was turned off"


class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Room 01 Speaker")

    def turn_on(self):
        return f"{self.name} is now ready to play music"

    def turn_off(self):
        return f"{self.name} stopped playing and was turned off"


class SmartFridge(SmartDevice):
    def __init__(self):
        super().__init__("Smart Fridge Model X")

    def turn_on(self):
        return f"{self.name} is now operating at optimal temperature"

    def turn_off(self):
        return f"{self.name} cooling system was turned off"


class SmartThermostat(SmartDevice):
    def __init__(self):
        super().__init__("Smart Thermostat")

    def turn_on(self):
        return f"{self.name} is set to 22 degrees Celsius"

    def turn_off(self):
        return f"{self.name} was turned off"


class SmartCamera(SmartDevice):
    def __init__(self):
        super().__init__("Front Door Camera")

    def turn_on(self):
        return f"{self.name} is recording and monitoring the entrance"

    def turn_off(self):
        return f"{self.name} stopped recording and was turned off"


# GUI with tkinter
class PolymorphicAppTemplate(tk.Tk):
    def __init__(self):
        super().__init__()

        # --- 1. WINDOW SETTINGS---
        self.title("OOP Lab: Polymorphism GUI Template")
        self.geometry("520x520")
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

        self.window_icon = tk.PhotoImage(width=16, height=16)
        self.window_icon.put("#111111", to=(0, 0, 15, 15))
        self.window_icon.put("#ffffff", to=(3, 3, 12, 12))
        self.window_icon.put("#111111", to=(6, 6, 9, 9))
        self.iconphoto(True, self.window_icon)

        # --- 2. OBJECT REGISTRY---
        # Map a friendly Radiobutton label to an instantiated object:
        self.items = {
            "Smart Speaker": SmartSpeaker(),
            "Smart Fridge": SmartFridge(),
            "Smart Light": SmartLight(),
            "Smart Thermostat": SmartThermostat(),
            "Smart Camera": SmartCamera(),
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

        self.btn_turn_off = tk.Button(
            self.controls,
            text="TURN OFF",
            command=self._handle_turn_off,
            font=("DejaVu Sans", 11, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=6,
        )
        self.btn_turn_off.pack(side="left", padx=5)

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

        self.lbl_log = tk.Label(
            self,
            text="ACTIVITY LOG",
            font=("DejaVu Sans", 11, "bold"),
        )
        self.lbl_log.pack(anchor="w", padx=20, pady=(8, 2))

        self.activity_log = tk.Listbox(
            self,
            height=6,
            font=("DejaVu Sans", 10),
            relief="flat",
        )
        self.activity_log.pack(fill="both", expand=True, padx=20, pady=(0, 12))
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
        self.btn_turn_off.configure(
            bg=colors["surface"],
            fg=colors["text"],
            activebackground=colors["output"],
            activeforeground=colors["text"],
            highlightbackground=colors["border"],
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
        self.lbl_log.configure(bg=colors["background"], fg=colors["text"])
        self.activity_log.configure(
            bg=colors["surface"],
            fg=colors["text"],
            selectbackground=colors["button"],
            selectforeground=colors["button_text"],
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
        self._run_device_action("turn_on")

    def _handle_turn_off(self):
        self._run_device_action("turn_off")

    def _run_device_action(self, action_name: str):
        chosen_key = self.selected_key.get()
        active_object: SmartDevice = self.items[chosen_key]
        result_message = getattr(active_object, action_name)()

        self.lbl_output.config(text=result_message, font=("DejaVu Sans", 12, "normal"))
        self.activity_log.insert(0, result_message)


# =====================================================================
# LAUNCHER
# =====================================================================
if __name__ == "__main__":
    app = PolymorphicAppTemplate()
    app.mainloop()
