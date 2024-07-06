import tkinter as tk
import random
import string
import pyperclip # Using this module to copy the generated password.

def generate_password():
    # Get the length entered by the user
    length = length_entry.get()
    if length.isdigit():
        length = int(length)
        # Combine letters, digits, and punctuation for password characters
        characters = string.ascii_letters + string.digits + string.punctuation
        # Generate a random password of the specified length
        password = ''
        for i in range(length):
            password += random.choice(characters) # to summarize it-> password = ''.join(random.choice(characters) for i in range(length)) can also be utilized.

        # Set the generated password to the StringVar
        password_var.set(password)
    else:
        # Set an error message if the input is not a valid number
        password_var.set("Invalid input")

def copy_password():
    # Copy the generated password to the clipboard
    password = password_var.get()
    pyperclip.copy(password)
    
# Now adding colors to make it more appeling..
# Creating the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg='#f0f0f0') # background color Gray

# Frame for input and buttons
frame = tk.Frame(root, bg='#f0f0f0')
frame.pack(pady=20)

# Label and Entry for password length
length_label = tk.Label(frame, text="Enter password length:", font=("Helvetica", 12), bg='#f0f0f0', fg='#333333')
length_label.grid(row=0, column=0, padx=10, pady=5)

length_entry = tk.Entry(frame, font=("Helvetica", 12), bg='#ffffff', fg='#333333')
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Button to generate password
generate_button = tk.Button(frame, text="Generate Password", font=("Helvetica", 12), command=generate_password, bg='#4CAF50', fg='#ffffff')
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Variable to store the generated password
password_var = tk.StringVar()

# Label to display the generated password
password_label = tk.Label(frame, textvariable=password_var, font=("Helvetica", 12), bg='#f0f0f0', fg='#333333')
password_label.grid(row=2, column=0, columnspan=2, pady=5)

# Button to copy the generated password
copy_button = tk.Button(frame, text="Copy Password", font=("Helvetica", 12), command=copy_password, bg='#2196F3', fg='#ffffff')
copy_button.grid(row=3, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()

# example ->
# the copied password : 