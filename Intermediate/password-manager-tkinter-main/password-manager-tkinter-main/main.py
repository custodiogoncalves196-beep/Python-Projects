from tkinter import *
from tkinter import messagebox
from password import password_generator
import json

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

def generate_password():
    password = password_generator()

    password_entry.delete(0, END)
    password_entry.insert(0,password_generator())


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill all fields")
    else:
        try:
            with open("password.json", "r") as file:
                data = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            with open("password.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)

            with open("password.json", "w") as file:
                json.dump(data, file, indent=4)

        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()

def find_password():
    website = website_entry.get()
    try:
        with open("password.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "Please fill all fields")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo("Password Found", f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror("Error", "Please fill all fields")


#label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, sticky="e")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")

#entreis
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew")
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

#bott on
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="ew")
save_button = Button(text="Save")
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="ew")
add_button = Button(text="Add", command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")






window.mainloop()