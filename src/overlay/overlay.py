import tkinter as tk
from PIL import Image, ImageTk


class Overlay(tk.Tk):
    def __init__(self, image: Image):
        super().__init__()

        self.overrideredirect(1)

        self.wm_attributes('-topmost', 1)

        self.image = ImageTk.PhotoImage(image)

        self.label = tk.Label(self, image=self.image)
        self.label.pack()

    def update_image(self, image: Image):
        self.image = ImageTk.PhotoImage(image)
        self.label.config(image=self.image)
