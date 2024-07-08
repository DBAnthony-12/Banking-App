import tkinter as tk
from tkinter import messagebox
from tkinter import Frame, Label, Entry, Button
from tkinter import simpledialog
from datetime import datetime
import string
import random

class Register:
    def __init__(self, root, login_form):
        self.root = root
        self.login_form = login_form  # Reference to the login form
        self.root.title("Register")
        self.root.geometry("450x450")
        self.root.resizable(False, False)
        self.root.configure(bg="lightblue")
        

        font_style = ("Arial", 12)  # Define font style

        self.lbl_name = tk.Label(root, text="Name:", font=font_style)
        self.lbl_name.pack()
        self.entry_name = tk.Entry(root, font=font_style, width=30)
        self.entry_name.pack()

        self.lbl_surname = tk.Label(root, text="Surname:", font=font_style)
        self.lbl_surname.pack()
        self.entry_surname = tk.Entry(root, font=font_style, width=30)
        self.entry_surname.pack()

        self.lbl_email = tk.Label(root, text="Email:", font=font_style)
        self.lbl_email.pack()
        self.entry_email = tk.Entry(root, font=font_style, width=30)
        self.entry_email.pack()

        self.lbl_password = tk.Label(root, text="Password:", font=font_style)
        self.lbl_password.pack()
        self.entry_password = tk.Entry(root, show="*", font=font_style, width=30)
        self.entry_password.pack()

        self.lbl_cPass = tk.Label(root, text="Confirm Password:", font=font_style)
        self.lbl_cPass.pack()
        self.entry_cPass = tk.Entry(root, show="*", font=font_style, width=30)
        self.entry_cPass.pack()

        # Register Button
        btn_font_style = ("Arial", 12, "bold")  # Define font style for buttons
        self.btn_register = tk.Button(root, text="Register", font=btn_font_style, command=self.register, width=20)
        self.btn_register.pack(pady=(10, 10))

        self.btn_login = tk.Button(root, text="Login", font=btn_font_style, command=self.open_login_form, width=20)
        self.btn_login.pack(pady=(0, 10))

        self.btn_generate_password = tk.Button(root, text="Generate Password", font=font_style, command=self.generate_password, width=20)
        self.btn_generate_password.pack(pady=(10, 10))

    def generate_random_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    def generate_password(self):
        new_password = self.generate_random_password()
        self.entry_password.delete(0, tk.END)
        self.entry_password.insert(0, new_password)
        self.entry_cPass.delete(0, tk.END)
        self.entry_cPass.insert(0, new_password)
        messagebox.showinfo("Generated Password", f"New Password: {new_password}")


    def register(self):
        # Get email and password entered by the user
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        cPass = self.entry_cPass.get()

        if not name or not surname or not email or not password or not cPass:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        if password != cPass:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        # Save the credentials to a text file
        with open("user_credentials.txt", "a") as file:
           file.write(f"{name} {surname} {email} {password}\n")
        
        # Show registration success message
        messagebox.showinfo("Success", "Registration successful!")

        # Close the registration form and show the login form
        self.root.destroy()
        self.login_form.show_login()

    def open_login_form(self):
        self.root.destroy()
        self.login_form.show_login()

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("500x200")
        self.root.resizable(False, False)
        self.root.configure(bg="lightblue")

        font_style = ("Arial", 12)  # Define font style

        # Labels and Entry Widgets for Email and Password
        self.lbl_email = tk.Label(root, text="Email:", font=font_style)
        self.lbl_email.pack()
        self.entry_email = tk.Entry(root, font=font_style, width=30)
        self.entry_email.pack()

        self.lbl_password = tk.Label(root, text="Password:", font=font_style)
        self.lbl_password.pack()
        self.entry_password = tk.Entry(root, show="*", font=font_style, width=30)
        self.entry_password.pack()

        # Login Button
        btn_font_style = ("Arial", 12, "bold") 
        self.btn_login = tk.Button(root, text="Login", font=btn_font_style, command=self.login, width=20)
        self.btn_login.pack(pady=(10, 10))

        # Register Button
        self.btn_register = tk.Button(root, text="Register", font=btn_font_style, command=self.open_register_form, width=20)
        self.btn_register.pack(pady=(0, 10))

    def login(self):
        # Get email and password entered by the user
        email = self.entry_email.get()
        password = self.entry_password.get()

        if not email or not password:
            messagebox.showerror("Error", "All fields are required!")
            return
        
        email_exists = False

        # Check if the credentials match any entry in the text file
        with open("user_credentials.txt", "r") as file:
            for line in file:
                try:
                    name, surname, stored_email, stored_password = line.strip().split()
                    if email == stored_email:
                        email_exists = True
                        if password == stored_password:
                            messagebox.showinfo("Welcome", f"Welcome {name} {surname}")
                            self.open_bank_application() 
                            return
                        else:
                            messagebox.showerror("Error", "Incorrect password")
                            return
                except ValueError:
                    continue  # Skip any lines that do not have exactly four values

        # If no matching email is found, show an error message
        if not email_exists:
            messagebox.showerror("Error", "Invalid email or password")
        
    def open_bank_application(self):
        self.root.withdraw()  # Hide the login window
        bank_app = BankApplication(self)  # Open the banking application
        bank_app.mainloop()

    def open_register_form(self):
        self.root.withdraw()  # Hide the login form
        register_root = tk.Tk()
        Register(register_root, self)  # Pass the Login form instance
        register_root.mainloop()

    def show_login(self):
        self.root.deiconify()  # Show the login form

class BankApplication(tk.Tk):
    def __init__(self, login_form):
        super().__init__()
        self.login_form = login_form
        self.title("Bank Application")
        self.geometry("400x200")
        self.resizable(False, False)
        self.configure(bg="purple")

        self.balance = 1000  # Initial balance
        bg_color = "lightblue"

        self.label_balance = tk.Label(self, text=f"Current Balance: ${self.balance}", bg=bg_color)
        self.label_balance.pack(pady=(10,10))

        self.button_transaction = tk.Button(self, text="Make a Transaction", command=self.transaction, width=20, bg="lightgrey")
        self.button_transaction.pack(pady=(10,10))

        self.button_view_history = tk.Button(self, text="View Transaction History", command=self.view_transaction_history, width=20, bg="lightgrey")
        self.button_view_history.pack()

    def transaction(self):
        response = messagebox.askquestion("Transaction", "Would you like to make a transaction?")
        if response == "yes":
            transaction_type = simpledialog.askstring("Transaction Type", "Would you like to make a deposit or withdrawal?")
            if transaction_type is not None:
                transaction_type = transaction_type.lower()  # Convert to lowercase for consistent comparison
                if transaction_type == "deposit":
                    amount = simpledialog.askfloat("Deposit Amount", "How much would you like to deposit?")
                    if amount is not None and amount > 0:
                        self.make_deposit(amount)
                        self.write_transaction_to_file("deposit", amount)
                    else:
                        messagebox.showerror("Error", "You provided an invalid input.")
                elif transaction_type == "withdrawal":
                    amount = simpledialog.askfloat("Withdrawal Amount", "How much would you like to withdraw?")
                    if amount is not None and amount > 0:
                        self.make_withdrawal(amount)
                        self.write_transaction_to_file("withdrawal", amount)
                    else:
                        messagebox.showerror("Error", "You provided an invalid input.")
                else:
                    messagebox.showerror("Transaction", "Invalid transaction type.")
            else:
                messagebox.showerror("Transaction", "No transaction made.")

    def make_deposit(self, amount):
        self.balance += amount
        messagebox.showinfo("Success", f"Deposit successful! New Balance: ${self.balance}")
        self.label_balance.config(text=f"Current Balance: ${self.balance}")
        self.write_transaction_to_file("Deposit", amount)

    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            messagebox.showinfo("Success", f"Withdrawal successful! New Balance: ${self.balance}")
            self.label_balance.config(text=f"Current Balance: ${self.balance}")
            self.write_transaction_to_file("Withdrawal", amount)
        else:
            messagebox.showerror("Error", "Insufficient balance!")

    def write_transaction_to_file(self, transaction_type, amount):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("TransactionLog.txt", "a") as file:
            file.write(f"{current_datetime} - {transaction_type.capitalize()}: ${amount}\n")

    def view_transaction_history(self):
        try:
            with open("TransactionLog.txt", "r") as file:
                transaction_history = file.read()
            messagebox.showinfo("Transaction History", transaction_history)
        except FileNotFoundError:
            messagebox.showerror("Error", "Transaction history file not found.")

if __name__ == "__main__":
    root = tk.Tk()
    login_form = Login(root)
    root.mainloop()
