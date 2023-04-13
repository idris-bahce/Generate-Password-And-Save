from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', '0', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_letters = [random.choice(letters) for i in range(nr_letters)]
password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
password_numbers = [random.choice(numbers) for i in range(nr_numbers)]
password_list = password_numbers + password_symbols + password_letters

random.shuffle(password_list)
password_generated = "".join(password_list)


def add_password():
    password_entry.insert(END, string=password_generated)
    pyperclip.copy(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website_name = website_entry.get()
    username_name = username_entry.get()
    passwords = password_entry.get()

    if len(website_name) == 0:
        messagebox.showerror(title="ERROR", message="Please fill website box!")
    elif len(passwords) == 0:
        messagebox.showerror(title="ERROR", message="Please fill password box!")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are details entered:"
                                                                   f" \nEmail: {username_name}\nPassword: {passwords}")

        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_name} | {username_name} | {passwords}\n")
            website_entry.delete(0, last=END)
            password_entry.delete(0, last=END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website = Label(text="Website: ")
website.grid(row=1, column=0)

email = Label(text="Email/Username: ")
email.grid(row=2, column=0)

password = Label(text="Password: ")
password.grid(row=3, column=0)

website_entry = Entry()
website_entry.config(width=52)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry()
username_entry.config(width=52)
username_entry.insert(END, string="someexp@user.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry()
password_entry.config(width=33)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=add_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save_data)
add_button.config(width=44)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
