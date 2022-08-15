from tkinter import *

window = Tk()
window.title("My First GUI Program.")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
first_label = Label(text="My First Label.", font=("Arial", 24, "bold"))
first_label.grid(column=0, row=0)
# first_label.pack(side="left")
# first_label.place(x=0, y=100)


first_label['text'] = "New Text"


def button_clicked():
    first_label.config(text=input_box.get())
    

# Button
first_btn = Button(text="Button", command=button_clicked)
first_btn.grid(column=1, row=1)
# first_btn.pack()

second_btn = Button(text="New Button", command=button_clicked)
second_btn.grid(column=2, row=0)

# Entry
input_box = Entry(width=10)
input_box.grid(column=3, row=2)
# input_box.pack()

#Text Box
# text = Text(width=30, height=5)
# text.insert(END, "Something Massage...")
# text.focus()
# text.pack()

# #Spinbox
# def spinbox_func():
#     print(spinbox.get())

# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_func)
# spinbox.pack()

# #Scale
# def scale_func(value):
#     print(value)

# scale = Scale(from_=0, to=100, command=scale_func)
# scale.pack()

# #Checkbox
# def checkbox_func():
#     print(checked_state.get())

# checked_state = IntVar(value=1)
# checkbox = Checkbutton(text="It On?", variable=checked_state, command=checkbox_func)
# checkbox.pack()

# #RadioButton
# def radio_func():
#     print(radio_state.get())

# radio_state = IntVar()
# radio_button1 = Radiobutton(text="Option1", variable=radio_state, value=1, command=radio_func)
# radio_button2 = Radiobutton(text="Option2", variable=radio_state, value=2, command=radio_func)
# radio_button3 = Radiobutton(text="Option3", variable=radio_state, value=3, command=radio_func)

# radio_button1.pack()
# radio_button2.pack()
# radio_button3.pack()

# # ListBox
# def listbox_func(event):
#     print(listbox.get(listbox.curselection()))

# fruits = ['Banana', 'Apple', 'Orange', 'Mango']
# listbox = Listbox(height=4)
# [listbox.insert(fruits.index(fruit), fruit) for fruit in fruits]
# listbox.bind("<<ListboxSelect>>", listbox_func)
# listbox.pack()


window.mainloop()