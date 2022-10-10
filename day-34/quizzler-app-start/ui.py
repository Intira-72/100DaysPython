from tkinter import *


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz_brain = quiz_brain

        self.gui = Tk()
        self.gui.title("Quizzler")
        self.gui.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_board = Label(self.gui, text=f"Score : 0", bg=THEME_COLOR, fg="white")
        self.score_board.grid(row=0, column=1)        

        self.canvas = Canvas(width=300, height=250)
        self.quiz = self.canvas.create_text(150, 125, width=280, text="", font=("Arial", 18, "italic"), fill=THEME_COLOR)
        self.canvas.grid(pady=50, row=1, column=0, columnspan=2)

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, borderwidth=0, command=self.true_answer)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=false_img, highlightthickness=0, borderwidth=0, command=self.false_answer)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()

        self.gui.mainloop()


    def get_next_question(self):
        self.canvas.configure(background="white")
        self.canvas.itemconfig(self.quiz, fill=THEME_COLOR)
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.quiz, text=q_text)           
        else:
            self.canvas.itemconfig(self.quiz, text="You've reached the end of the quiz.")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    
    def true_answer(self):
        answer = self.quiz_brain.check_answer("True")
        self.get_affact_canvas(answer)


    def false_answer(self):
        answer = self.quiz_brain.check_answer("False")
        self.get_affact_canvas(answer)


    def get_affact_canvas(self, answer):
        self.canvas.itemconfig(self.quiz, fill="white")

        if answer:
            self.canvas.configure(background="green")
            self.score_board.configure(text=f"Score : {answer}")
        else:
            self.canvas.configure(background="red")
        
        self.gui.after(1000, func=self.get_next_question)