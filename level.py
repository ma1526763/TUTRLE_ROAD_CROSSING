from turtle import Turtle

def get_highest_level():
    try:
        with open("highest_level.txt") as file:
            return int(file.readline())
    except FileNotFoundError:
        with open("highest_level.txt", "w") as file:
            file.write("1")
            return 1

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.highest_level = get_highest_level()
        self.level_number = 1
        self.write_level_number()

    def write_level_number(self):
        self.clear()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Level # {self.level_number} ", align="center", font=("Arial", 24, "normal"))
        self.goto(270, 270)
        self.write(f"Best level: {self.highest_level}", font=("Arial", 10, "normal"))

    def update_level(self):
        self.level_number += 1
        self.write_level_number()

    def game_over(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write(f"GAME OVER !!!", align="center", font=("Arial", 24, "normal"))

    def update_highest_score(self):
        if self.level_number > self.highest_level:
            with open("highest_level.txt", "w") as file:
                file.write(str(self.level_number))
            self.highest_level = self.level_number
        self.level_number = 1
        self.write_level_number()
