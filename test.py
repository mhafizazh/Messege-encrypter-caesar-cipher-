import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import caecar_function_gui

window = ttk.Window(themename="cosmo")
window.geometry("1050x500")
window.title('Message encrypter tool')

def encrypt_input():
    words = text_box.get("1.0", tk.END)
    shift = int(shift_number_input.get("1.0", tk.END))
    encrypted_text = caecar_function_gui.encrypt(original_text=words, number_shift=shift)
    # text_box_output.delete(1.0, tk.END)  # Clear previous output
    text_box_output.insert(tk.END, encrypted_text)

def decrypt_input():
    words = text_box.get("1.0", tk.END)
    shift = int(shift_number_input.get("1.0", tk.END))
    decrypted_text = caecar_function_gui.decoded(encrypted_text=words, number_shift=shift)
    # text_box_output.delete(1.0, tk.END)  # Clear previous output
    text_box_output.insert(tk.END, decrypted_text)


text_box = tk.Text(window, height=17, width=40)
text_box.place(x=50, y=75)

text_box_output = tk.Text(window, height=17, width=40)
text_box_output.place(x=650, y=75)

shift_number_lbl = tk.Label(window, text="Shift : ")
shift_number_lbl.place(x=450, y=155)
shift_number_input = tk.Text(window, height=1, width=4)
shift_number_input.place(x=500, y=150)

encrypt_button = ttk.Button(window, text="Encrypt Message", command=encrypt_input)
encrypt_button.place(x=450, y=200)

decrypt_button = ttk.Button(window, text="Decrypt Message", command=decrypt_input)
decrypt_button.place(x=450, y=250)

window.mainloop()
