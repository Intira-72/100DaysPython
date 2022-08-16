from cgitb import text
import math
import tkinter as tk


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)

    label_status.config(text="Timer")
    label_brake.config(text="")
    canvas.itemconfig(time_text, text="00:00")

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1   

    if reps == 8:
        label_status.config(text="Long Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        label_status.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        label_status.config(text="Work Min", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60

    canvas.itemconfig(time_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()

        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark = "✔"

        label_brake.config(text=mark)
    

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=80, pady=50, bg=YELLOW)

label_status = tk.Label(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN, bg=YELLOW)
label_status.grid(column=1, row=0)

img = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=202, height=224,bg=YELLOW, highlightthickness=0)
canvas.create_image(101, 112, image=img)
time_text = canvas.create_text(101, 135, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(column=1, row=1)

label_brake = tk.Label(font=(FONT_NAME, 14, "bold"), fg=GREEN, bg=YELLOW)
label_brake.grid(column=1, row=3)

btn_start = tk.Button(text="Start", width=10, command=start_timer)
btn_start.grid(column=0, row=2)

btn_reset = tk.Button(text="Reset", width=10, command=reset_timer)
btn_reset.grid(column=2, row=2)




window.mainloop()