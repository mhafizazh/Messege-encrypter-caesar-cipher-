import tkinter as tk
from tkinter import ttk

def open_popup():
    popup = tk.Toplevel(root)
    popup.title("Popup Window")

    label = ttk.Label(popup, text="This is a popup window.")
    label.pack(padx=10, pady=10)

    close_button = ttk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

    # Make the popup modal
    popup.grab_set()

root = tk.Tk()
root.title("Main Window")

popup_button = ttk.Button(root, text="Open Popup", command=open_popup)
popup_button.pack(padx=10, pady=10)

root.mainloop()
