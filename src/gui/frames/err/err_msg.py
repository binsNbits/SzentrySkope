import customtkinter
import tkinter as tk
from constants.constants import (
    PADY_1, NSEW, PADX_1
)

class ErrMsg(customtkinter.CTkToplevel):
    def __init__(self, message="An Error Occurred", main_window=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x200")

        self.main_window = main_window  # Store a reference to the main window

        self.msg = message
        self.label = customtkinter.CTkLabel(self, bg_color="red", font=("Arial", 16, "bold"), text=self.msg)
        self.label.pack(padx=20, pady=20)

        self.protocol("WM_DELETE_WINDOW", self.on_close)  # Handle window close event

        self.close_button = tk.Button(self, text="Close", command=self.on_close)
        self.close_button.pack(pady=10)

    def on_close(self):
        
        self.destroy()  # Destroy the error message window




