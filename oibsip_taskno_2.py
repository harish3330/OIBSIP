import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12):
    if length < 8:
        messagebox.showerror("Invalid Length", "Password length should be at least 8 characters.")
        return None
    
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    all_characters = lower_case + upper_case + digits + special_characters
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def generate_password_gui():
    try:
        length = int(entry_length.get())
        password = generate_password(length)
        
        if password:
            label_result.config(text=f"Generated Password: {password}", fg="white", bg="#4CAF50", font=("Helvetica", 14, "bold"))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")
        
# main window
root = tk.Tk()
root.title("Simple Password Generator")
root.geometry("400x300")  # Window size
root.config(bg="#2C3E50")  # Dark background for the window

# Custom fonts
font_label = ("Helvetica", 12)
font_button = ("Helvetica", 12, "bold")

# instructions label
label_instruction = tk.Label(root, text="Enter Password Length (min 8):", fg="white", bg="#2C3E50", font=font_label)
label_instruction.pack(pady=20)

# Entry for password length
entry_length = tk.Entry(root, font=("Helvetica", 12), width=15, bd=2, relief="solid", fg="#2C3E50", bg="#ECF0F1")
entry_length.pack(pady=10)

# Generate button
button_generate = tk.Button(root, text="Generate Password", font=font_button, bg="#3498DB", fg="white", command=generate_password_gui)
button_generate.pack(pady=10, ipady=5, ipadx=10)

# Label to display the generated password
label_result = tk.Label(root, text="Generated Password: ", fg="white", bg="#2C3E50", font=("Helvetica", 14))
label_result.pack(pady=10)

# GUI event loop
root.mainloop()
