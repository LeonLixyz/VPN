#!/usr/bin/env python3
import tkinter as tk

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Hello World")

    # Create a label widget with the message
    message = tk.Label(root, text="Hello, world!", font=("Arial", 16))
    message.pack(padx=20, pady=20)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
