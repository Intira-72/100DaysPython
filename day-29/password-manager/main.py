import tkinter as tk
import random
from tkinter import messagebox
import pyperclip


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
    
    if "" in [user, password, website]:
        messagebox.showwarning(title="Value is empty!", message="Please don't leave any fields empty!")
    else:
        msg = messagebox.askokcancel(title=input_web.get(), message=f"These are the details entered: \nEmail: {input_username.get()} \nPassword: {input_password.get()} \nIs it OK to Save?")
        if msg:
            with open('data.txt', 'a') as file:
                file.write(f'{input_web.get()} | {input_username.get()} | {input_password.get()}')
                file.write('\n')

                input_web.delete(0, 'end')
                input_password.delete(0, 'end')

                input_username.delete(0, 'end')
                input_username.insert(0, "@gmail.com")

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

input_web = tk.Entry(width=50)
input_web.focus()
input_web.grid(row=1, column=1, columnspan=2)

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

btn_add = tk.Button(text="Add", width=42, command=save_data)
btn_add.grid(row=4, column=1, columnspan=2, pady=5)

window.mainloop()