from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
data = pd.read_csv("data/eng_words.csv", encoding="TIS-620")
to_learn = data.to_dict(orient="records") # exp. {'eng_lang': 'accept', 'thai_lang': 'ยอมรับ'}
current_card = {}


def next_card():
    global current_card, flip_timer
    gui.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='[ English ]', fill="black")
    canvas.itemconfig(card_word, text=current_card['eng'], fill="black")    
    canvas.itemconfig(card_bg, image=card_front_img)  

    flip_timer = gui.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="[ Thai ]", fill="white")
    canvas.itemconfig(card_word, text=current_card['thai'], fill="white")    
    canvas.itemconfig(card_bg, image=card_back_img)


def is_know():
    to_learn.remove(current_card)
    print(len(to_learn))
    next_card()


gui = Tk()
gui.title("Flash Cards (ENG)")
gui.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = gui.after(3000, func=flip_card)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 120, text="", font=("Ariel", 32, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_img, highlightthickness=0, borderwidth=0, command=flip_card)
unknown_btn.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
check_btn = Button(image=right_img, highlightthickness=0, borderwidth=0, command=is_know)
check_btn.grid(row=1, column=1)

next_card()

gui.mainloop()