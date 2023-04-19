import tkinter as tk
from tkinter import ttk
import os

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Main Menu")
        self.master.geometry("400x300")

        # Create the "Product Analytics" button
        self.analytics_button = ttk.Button(self.master, text="Product Analytics", command=self.open_analytics, style="main.TButton")
        self.analytics_button.pack(pady=(50, 10))

        # Create the "Show Images" button
        self.images_button = ttk.Button(self.master, text="Show Images", command=self.open_images, style="main.TButton")
        self.images_button.pack(pady=10)

        # Create a custom style for the buttons
        style = ttk.Style()
        style.configure("main.TButton", font=("Helvetica", 14), foreground="#fff", background="#2e8b57", borderwidth=0, width=20)

    def open_analytics(self):
        # Open the "analytics.py" file using the default application
        os.system("python productanalytics.py")

    def open_images(self):
        # Open the "imagegallery.py" file using the default application
        os.system("python imagegallery.py")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
