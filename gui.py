import subprocess
import tkinter as tk
from tkinter import filedialog


def encrypt_file(input_file, output_file, recipient):
    try:
        subprocess.run(
            ['gpg', '--output', output_file, '--encrypt', '--recipient', recipient, input_file],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        show_message("Success", f"File '{input_file}' successfully encrypted to '{output_file}'")
    except subprocess.CalledProcessError as e:
        error_message = e.stderr.strip()
        show_message("Error", f"Error encrypting file:\n{error_message}")


def browse_file(entry):
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)


def save_file(entry):
    filename = filedialog.asksaveasfilename(defaultextension=".gpg",
                                            filetypes=[("GPG files", "*.gpg"), ("All files", "*.*")])
    entry.delete(0, tk.END)
    entry.insert(0, filename)


def show_message(title, message):
    top = tk.Toplevel()
    top.title(title)
    top.resizable(False, False)
    message_label = tk.Label(top, text=message, padx=20, pady=20, wraplength=300)
    message_label.pack()
    tk.Button(top, text="OK", command=top.destroy).pack(pady=10)
    top.grab_set()  # Make the dialog modal
    top.update_idletasks()
    top.geometry(
        f"{top.winfo_width()}x{top.winfo_height()}+{int(root.winfo_screenwidth() / 2 - top.winfo_reqwidth() / 2)}+{int(
            root.winfo_screenheight() / 2 - top.winfo_reqheight() / 2)}")
    root.wait_window(top)


def on_encrypt():
    input_file = input_entry.get()
    output_file = output_entry.get()
    recipient = recipient_entry.get()
    if not input_file or not output_file or not recipient:
        show_message("Input Error", "Please fill all fields")
        return
    encrypt_file(input_file, output_file, recipient)


root = tk.Tk()
root.title("GPG Encryptor")
root.resizable(False, False)
tk.Label(root, text="Input File:").grid(row=0, column=0, padx=10, pady=10)
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=lambda: browse_file(input_entry)).grid(row=0, column=2, padx=10, pady=10)
tk.Label(root, text="Output File:").grid(row=1, column=0, padx=10, pady=10)
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Save As", command=lambda: save_file(output_entry)).grid(row=1, column=2, padx=10, pady=10)
tk.Label(root, text="Recipient Email:").grid(row=2, column=0, padx=10, pady=10)
recipient_entry = tk.Entry(root, width=50)
recipient_entry.grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Encrypt", command=on_encrypt).grid(row=3, columnspan=3, pady=20)
root.mainloop()
