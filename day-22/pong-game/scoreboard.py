from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Conrier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()

        self.goto(-50, 250)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)

        self.goto(0, 250)
        self.write(f":", align=ALIGNMENT, font=FONT)

        self.goto(50, 250)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)


    def r_points(self):
        self.r_score += 1
        self.update_scoreboard()


    def l_points(self):
        self.l_score += 1
        self.update_scoreboard()

