import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x400")
        self.root.config(bg="#f0f0f0")

        # Setting up the label for title
        self.title_label = tk.Label(root, text="Password Generator", font=("Arial", 18, 'bold'), bg="#f0f0f0", fg="#333")
        self.title_label.pack(pady=20)

        # Length input
        self.length_label = tk.Label(root, text="Enter password length:", bg="#f0f0f0", font=("Arial", 12))
        self.length_label.pack(pady=5)
        
        self.length_entry = tk.Entry(root, font=("Arial", 14), width=20, bd=2)
        self.length_entry.pack(pady=10)

        # Checkboxes for character set options
        self.upper_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)

        self.upper_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=self.upper_var, bg="#f0f0f0", font=("Arial", 12))
        self.upper_check.pack()

        self.digits_check = tk.Checkbutton(root, text="Include Digits", variable=self.digits_var, bg="#f0f0f0", font=("Arial", 12))
        self.digits_check.pack()

        self.special_check = tk.Checkbutton(root, text="Include Special Characters", variable=self.special_var, bg="#f0f0f0", font=("Arial", 12))
        self.special_check.pack()

        # Generate Button
        self.generate_button = tk.Button(root, text="Generate Password", font=("Arial", 14, 'bold'), bg="#4CAF50", fg="white", command=self.generate_password)
        self.generate_button.pack(pady=20)

        # Password display area
        self.result_label = tk.Label(root, text="Generated Password: ", bg="#f0f0f0", font=("Arial", 12))
        self.result_label.pack()

        self.password_display = tk.Label(root, text="", font=("Arial", 14, 'bold'), fg="#333")
        self.password_display.pack(pady=10)

    def generate_password(self):
        # Get password length from input
        try:
            length = int(self.length_entry.get())
            if length < 8:
                messagebox.showwarning("Invalid Length", "Password length should be at least 8 characters.")
                return
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number for password length.")
            return

        # Create character set based on user selection
        characters = string.ascii_lowercase  # Start with lowercase letters

        if self.upper_var.get():
            characters += string.ascii_uppercase
        if self.digits_var.get():
            characters += string.digits
        if self.special_var.get():
            characters += string.punctuation

        # Generate a random password from the selected characters
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display the generated password
        self.password_display.config(text=password)

# Create the main window
root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()
