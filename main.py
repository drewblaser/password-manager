import tkinter.messagebox
from tkinter import *
import password
import json

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open(file="data.json", mode="r") as web_data:
            data = json.load(web_data)
            user_data = data[website_entry.get().title()]
            web_data = data.keys()
    except FileNotFoundError:
        tkinter.messagebox.showinfo("Error", "No data file found")
    except KeyError:
        tkinter.messagebox.showinfo("Error", f"No details for {website_entry.get().title()} exists.")
    else:
        for key in web_data:
            if website_entry.get().title() == key:
                tkinter.messagebox.showinfo(website_entry.get(), f"The information for {website_entry.get().title()}"
                                                                 f" is:\n"
                                                                 f"Email: {user_data['Email']}\n"
                                                                 f"Password: {user_data['Password']}")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password():
    pw = password.pw_gen()
    password_entry.delete(0, END)
    password_entry.insert(0, pw)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def update_list():
    new_data = {
        website_entry.get().title(): {
            "Email": email_entry.get(),
            "Password": password_entry.get(),
        }
    }

    if password_entry.get() == '' or email_entry.get() == '' or website_entry.get() == '':
        tkinter.messagebox.showwarning("Error", "Please input all fields")
    else:
        try:
            with open(file='data.json', mode="r") as pw_data:
                # reading old data
                data = json.load(pw_data)
                # updating old with new data
        except FileNotFoundError:
            with open("data.json", "w") as pw_data:
                json.dump(new_data, pw_data, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as pw_data:
                json.dump(data, pw_data, indent=4)
        finally:

            tkinter.messagebox.showinfo("Success", "Your info was successfully stored!")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

generate_pw_button = Button(text="Generate Password", command=random_password)
generate_pw_button.grid(column=2, row=3)

add_button = Button(text="Add", width=33, command=update_list)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)


window.mainloop()