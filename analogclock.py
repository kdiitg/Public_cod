import tkinter as tk
import customtkinter as ctk
from datetime import datetime
import math

class NeedleClock:
    def __init__(self):
        ctk.set_appearance_mode("dark")  # Modes: "system" (default), "light", "dark"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

        self.root = ctk.CTk()
        self.root.title("Analog Clock")
        self.root.geometry("200x200")
        self.root.resizable(False, False)

        self.canvas = ctk.CTkCanvas(self.root, width=400, height=400, bg="black", highlightthickness=0)
        self.canvas.pack()

        self.center_x = 100
        self.center_y = 100
        self.clock_radius = 90

        self.create_clock_face()
        self.update_clock()

        self.root.mainloop()

    def create_clock_face(self):
        self.canvas.create_oval(self.center_x - self.clock_radius, self.center_y - self.clock_radius,
                                self.center_x + self.clock_radius, self.center_y + self.clock_radius,
                                outline="gray", width=2)
        for hour in range(12):
            angle = math.radians(hour * 30)
            x = self.center_x + self.clock_radius * 0.85 * math.sin(angle)
            y = self.center_y - self.clock_radius * 0.85 * math.cos(angle)
            self.canvas.create_text(x, y, text=str(hour if hour else 12), fill="gray", font=("Helvetica", 14))

    def update_clock(self):
        now = datetime.now()
        self.canvas.delete("hands")

        # Draw hour hand
        hour_angle = math.radians((now.hour % 12) * 30 + now.minute * 0.5)
        self.draw_hand(hour_angle, self.clock_radius * 0.5, 6)

        # Draw minute hand
        minute_angle = math.radians(now.minute * 6)
        self.draw_hand(minute_angle, self.clock_radius * 0.75, 4)

        # Draw second hand
        second_angle = math.radians(now.second * 6)
        self.draw_hand(second_angle, self.clock_radius * 0.85, 2, fill="red")

        self.root.after(1000, self.update_clock)

    def draw_hand(self, angle, length, width, fill="gray"):
        x = self.center_x + length * math.sin(angle)
        y = self.center_y - length * math.cos(angle)
        self.canvas.create_line(self.center_x, self.center_y, x, y, width=width, fill=fill, tags="hands")

if __name__ == "__main__":
    NeedleClock()
