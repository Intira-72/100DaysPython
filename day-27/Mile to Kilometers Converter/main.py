from tkinter import *


def calculate_mile_to_km():
    mile = float(en_mile.get())
    km = mile * 1.60934
    label_km.config(text=int(round(km)))


window = Tk()
window.title("Mile to Kilometers Converter")
# window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

en_mile = Entry(width=7)
en_mile.grid(column=1, row=0)

label_mile = Label(text="Miles.")
label_mile.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_km = Label(text="0")
label_km.grid(column=1, row=1)

label_unit = Label(text="Km.")
label_unit.grid(column=2, row=1)

btn_cal = Button(text="Calculate", command=calculate_mile_to_km)
btn_cal.grid(column=1, row=2)


window.mainloop()