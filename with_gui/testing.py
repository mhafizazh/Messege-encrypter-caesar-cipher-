import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import caecar_function_gui

window = ttk.Window(themename="cosmo")
window.geometry("1050x500")
window.title('Message encrypter tool')

def invalid_shift():
    popup = tk.Toplevel(window)
    popup.title("Popup Window")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the position to center the popup window
    popup_width = 300  # Specify the width of the popup
    popup_height = 100  # Specify the height of the popup
    x_position = (screen_width - popup_width) // 2
    y_position = (screen_height - popup_height) // 2

    # Set the geometry of the popup window
    popup.geometry(f"{popup_width}x{popup_height}+{x_position}+{y_position}")

    label = ttk.Label(popup, text="Please input invalid number")
    label.pack(padx=10, pady=10)

    close_button = ttk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

    # Make the popup modal
    popup.grab_set()

def clear_bttn():
    text_box.delete("1.0", tk.END)
    text_box_output.delete("1.0", tk.END)
    shift_number_input.delete("1.0", tk.END)

def encrypt_input():
    try:
        words = text_box.get("1.0", tk.END)
        shift = int(shift_number_input.get("1.0", tk.END))
        encrypted_text = caecar_function_gui.encrypt(original_text=words, number_shift=shift)
        text_box_output.delete(1.0, tk.END)  # Clear previous output
        text_box_output.insert(tk.END, encrypted_text)
    except ValueError:
        invalid_shift()


def decrypt_input():
    try:
        words = text_box.get("1.0", tk.END)
        shift = int(shift_number_input.get("1.0", tk.END))
        decrypted_text = caecar_function_gui.decoded(encrypted_text=words, shift=shift)

        # Check if decrypted_text is None and convert to an empty string if needed
        if decrypted_text is None:
            decrypted_text = ""
        else:
            text_box_output.delete(1.0, tk.END)  # Clear previous output
            text_box_output.insert(tk.END, decrypted_text)
    except ValueError:
        invalid_shift()


text_box = tk.Text(window, height=17, width=40)
# text_box.grid(row=1, column=3)
# text_box.place(x=50, y=75)
text_box.grid(row=0, column=0, padx=1, pady=1)

text_box_output = tk.Text(window, height=17, width=40)
# text_box_output.place(x=650, y=75)
# text_box.grid(row=4, column=1)

shift_number_lbl = tk.Label(window, text="Shift : ")
# shift_number_lbl.place(x=450, y=155)
shift_number_input = tk.Text(window, height=1, width=4)
# shift_number_input.place(x=500, y=150)

encrypt_button = ttk.Button(window, text="Encrypt Message", command=encrypt_input)
# encrypt_button.place(x=450, y=200)

decrypt_button = ttk.Button(window, text="Decrypt Message", command=decrypt_input)
# decrypt_button.place(x=450, y=250)

clear_button = ttk.Button(window, text="Clear", command=clear_bttn)
# clear_button.place(x=484,y=300)




window.mainloop()
