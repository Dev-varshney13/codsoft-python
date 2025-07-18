import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x260")
root.configure(bg="#7c5c3b")  # Deep wood brown

# Frame for a "panel" effect
panel = tk.Frame(root, bg="#bfa171", bd=4, relief="ridge")
panel.place(relx=0.5, rely=0.5, anchor="center", width=370, height=220)

tk.Label(
    panel, text="Enter password length:",
    font=("Arial", 12, "bold"),
    bg="#bfa171", fg="#4e2e0e"  # Medium wood, dark brown text
).pack(pady=10)

length_entry = tk.Entry(
    panel, font=("Arial", 12), width=10, justify='center',
    bg="#e6ccb2", fg="#4e2e0e", insertbackground="#4e2e0e"  # Light wood, dark brown text/cursor
)
length_entry.pack(pady=5)

tk.Button(
    panel, text="Generate Password", font=("Arial", 12, "bold"),
    bg="#a47551", fg="#fff", activebackground="#8b5c2d", activeforeground="#fff",
    command=generate_password
).pack(pady=10)

password_var = tk.StringVar()
password_entry = tk.Entry(
    panel, textvariable=password_var, font=("Arial", 14), width=30,
    justify='center', state='readonly', bg="#f5e6da", fg="#4e2e0e"  # Very light wood, dark brown text
)
password_entry.pack(pady=10)

tk.Button(
    panel, text="Copy to Clipboard", font=("Arial", 8, "bold"),
    bg="#e6ccb2", fg="#4e2e0e",  # Light wood background, dark brown text
    activebackground="#a47551", activeforeground="#fff",
    command=copy_password, width=20, height=7, bd=3, relief="raised"
).pack(pady=10)

root.mainloop()