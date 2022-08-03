from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Conrier", 18, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.high_score = 0
        
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

        

    def update_scoreboard(self):
        self.clear()
        self.write(f"High Score: {self.high_score} | Score: {self.score}", align=ALIGNMENT, font=FONT)   


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER.", align=ALIGNMENT, font=FONT)