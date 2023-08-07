import tkinter as tk
from PIL import Image, ImageTk


class Overlay(tk.Tk):
    def __init__(self, image_path):
        super().__init__()

        self.overrideredirect(1)

        self.wm_attributes('-topmost', 1)

        image = Image.open(image_path)
        self.image = ImageTk.PhotoImage(image)

        self.label = tk.Label(self, image=self.image)
        self.label.pack()

    def update_image(self, image_path):
        image = Image.open(image_path)
        self.image = ImageTk.PhotoImage(image)
        self.label.config(image=self.image)
