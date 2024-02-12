import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length < 1:
        result_label.config(text="Please enter a valid length", fg="red")
        return
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=password_length))
    result_label.config(text="Generated Password: " + password, fg="blue")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#f0f0f0")

# Label and entry for username
username_label = tk.Label(root, text="Enter User Name:", font=("Arial", 20), bg="#f0f0f0")
username_label.pack()
username_entry = tk.Entry(root, font=("Arial", 20))
username_entry.pack()

# Label and entry for password length
length_label = tk.Label(root, text="Enter password length:", font=("Arial", 20), bg="#f0f0f0")
length_label.pack()
length_entry = tk.Entry(root, font=("Arial", 20))
length_entry.pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 16), bg="#4CAF50", fg="white")
generate_button.pack()

# Label to display generated password
result_label = tk.Label(root, text="", font=("Arial", 20), bg="#f0f0f0")
result_label.pack()

root.mainloop()