import tkinter as tk
import customtkinter as ctk
from datetime import datetime
import time
import threading

class DigitalClock:
    def __init__(self):
        ctk.set_appearance_mode("dark")  # Modes: "system" (default), "light", "dark"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

        self.root = ctk.CTk()
        self.root.title("Digital Clock")
        self.root.geometry("250x100")

        self.time_label = ctk.CTkLabel(self.root, text="", font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.update_time()
        
        self.root.mainloop()

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.time_label.configure(text=current_time)
        self.root.after(500, self.update_time)

if __name__ == "__main__":
    DigitalClock()
