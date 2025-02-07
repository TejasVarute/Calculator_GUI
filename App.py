import customtkinter as ctk
from calculator import Calculator

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("300x450")
        self.resizable(False, False)
        self.iconbitmap("icon.ico")
        self.entry_var = ctk.StringVar()
        
        self.entry_box()
        self.apear_button = ctk.CTkButton(self.entry_frame, text="Theme", corner_radius=20, font=("Arial", 18), width=60, command=self.change_mode)
        self.apear_button.pack(pady=5, padx=10)
        self.keypad()

    def change_mode(self):
        ctk.set_appearance_mode("Dark" if ctk.get_appearance_mode() == "Light" else "Light")
        
    def entry_box(self):
        self.entry_frame = ctk.CTkFrame(self, width=300, height=100, corner_radius=10)
        self.entry_frame.pack(pady=20)
        self.entry = ctk.CTkEntry(self.entry_frame, textvariable=self.entry_var, corner_radius=10, font=("Arial", 20), height=100, width=290, justify="right")
        self.entry.pack()

    def keypad(self):
        def calculations(char):
            if char == "CC":
                self.entry_var.set("")
            elif char == "=":
                try:
                    result = Calculator(self.entry_var.get()).Calculate()               #We have predefined function as Eval which work same.
                    self.entry_var.set(str(result))
                except Exception:
                    self.entry_var.set("Error")
            else:
                self.entry_var.set(self.entry_var.get() + char)
    
        self.button_frame = ctk.CTkFrame(self, width=290, height=380)
        self.button_frame.pack(padx=10, pady=10)
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("CC", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]
        
        for (text, row, col) in buttons:
            btn = ctk.CTkButton(self.button_frame, text=text, font=("Arial", 18), width=60, height=50, command=lambda new_text = text: calculations(new_text))
            btn.grid(row=row, column=col, padx=5, pady=5)

CalculatorApp().mainloop()