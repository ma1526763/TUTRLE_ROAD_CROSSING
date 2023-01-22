from turtle import Turtle
class Racer(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.goto(0, -270)

    def move_race(self, screen):
        screen.listen()
        screen.onkeypress(key="Up", fun=self.move_race_up)
        screen.onkeypress(key="w", fun=self.move_race_up)
        screen.onkeypress(key="W", fun=self.move_race_up)

    def move_race_up(self):
        self.forward(20)

    def reset_racer_position(self):
        self.goto(0, -270)