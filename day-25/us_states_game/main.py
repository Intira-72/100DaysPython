from __future__ import barry_as_FLUFL
import turtle
import pandas

IMG = "blank_states_img.gif"
FONT = ("Courier", 10, "bold")
ALIGNMENT = "center"

screen = turtle.Screen()
screen.title("U.S. States Game.")
screen.setup(width=760, height=520)
screen.addshape(IMG)

turtle.shape(IMG)

data = pandas.read_csv("50_states.csv")
answer_list = []


while len(answer_list) < 51:
    try:
        answer_state = screen.textinput(title=f"{len(answer_list)}/50 Guess the state", prompt="What's another state's name ?").title()
        data_check = data[data.state == answer_state]       

        if data_check.empty is not True and answer_state not in answer_list:   
            us_state = turtle.Turtle()          
            us_state.hideturtle()
            us_state.penup()
            us_state.goto(int(data_check.x), int(data_check.y))
            us_state.write(f"{data_check.state.item()}", align=ALIGNMENT, font=FONT)
            answer_list.append(data_check.state.item())
       
    except AttributeError:       
        turtle.write(f"GAME OVER. - {len(answer_list)} Score.", align=ALIGNMENT, font=FONT)

        states_to_learn = pandas.DataFrame({"states_to_learn": [x for x in data.state.to_list() if x not in answer_list]})
        states_to_learn.to_csv("States_to_learn.csv")

        break    


screen.exitonclick()