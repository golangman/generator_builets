import tkinter
from tkinter import Button, Entry, Frame, StringVar, messagebox

from database import DatabaseManager
from ui import Window


# label = tkinter.Label(root, text="Hello World!")  # Create a text label
# label.pack(padx=0, pady=0)  # Pack it into the window


def main(root):
    window = Window(root, db)
    window.login_page_init()
    root.eval("tk::PlaceWindow . center")

    root.mainloop()


if __name__ == "__main__":
    db = DatabaseManager()

    root = tkinter.Tk()

    main(root)
