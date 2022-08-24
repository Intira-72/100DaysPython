import tkinter as tk
import random
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    upper_chr = [chr(u) for u in range(65, 91)]
    lower_chr = [chr(l) for l in range(97, 123)]
    num = [str(n) for n in range(0, 10)]
    symbols = [chr(s) for s in range(33, 39)]

    password_list = []

    for password_position in range(12):
        pass_gen = random.choice(random.choice([upper_chr, lower_chr, num, symbols]))
        password_list.append(pass_gen)

    input_password.delete(0, 'end')
    input_password.insert('end', ''.join(password_list))

    pyperclip.copy(''.join(password_list))

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    user = input_username.get()
    password = input_password.get()
    website = input_web.get()

    new_data = {
        website: {
        'email': user,
        'pass': password
        }
    }   
    
    if "" in [user, password, website]:
        messagebox.showwarning(title="Value is empty!", message="Please don't leave any fields empty!")
    else:
        msg = messagebox.askokcancel(title=input_web.get(), message=f"These are the details entered: \nEmail: {input_username.get()} \nPassword: {input_password.get()} \nIs it OK to Save?")
        if msg:
            try:
                with open('data.json', 'r') as file:
                    # Reading old data
                    data = json.load(file)

                    # Updating old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open('data.json', 'w') as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            finally:
                clear()


# ---------------------------- CLEAR FORM ------------------------------- #
def clear():
    input_web.delete(0, 'end')
    input_password.delete(0, 'end')

    input_username.delete(0, 'end')
    input_username.insert(0, "@gmail.com")


# ---------------------------- SEARCH ------------------------------- #
def search():
    website = input_web.get()           
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)
            email = data[website]['email']
            passw = data[website]['pass']            
    except FileNotFoundError:
        messagebox.showwarning(title=website, message=f"No Data File Found.")
    except KeyError:
        messagebox.showwarning(title=website, message=f"No details for the {website} exits.")
    else:
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {passw}")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
# window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

img = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=0, columnspan=3)

lable_web = tk.Label(text="Website:")
lable_web.grid(row=1, column=0)

input_web = tk.Entry(width=31)
input_web.focus()
input_web.grid(row=1, column=1)

lable_username = tk.Label(text="Email / Username:")
lable_username.grid(row=2, column=0, pady=5, padx=5)

input_username = tk.Entry(width=50)
input_username.insert(0, "@gmail.com")
input_username.grid(row=2, column=1, columnspan=2, pady=5)

lable_password = tk.Label(text="Password:")
lable_password.grid(row=3, column=0)

input_password = tk.Entry(width=31)
input_password.grid(row=3, column=1)

btn_genpass = tk.Button(text="Generate Password", command=password_gen)
btn_genpass.grid(row=3, column=2)

btn_search = tk.Button(text="Search", width=15, command=search)
btn_search.grid(row=1, column=2, pady=5)

btn_add = tk.Button(text="Add", width=42, command=save_data)
btn_add.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()