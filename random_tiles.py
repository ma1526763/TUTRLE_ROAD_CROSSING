from turtle import Turtle
import random

COLOR_LIST = ["white", "blue", "green", "red", "orange", "yellow", "brown", "cyan", "khaki", "gold"]


class RandomTile:
    def __init__(self):
        self.random_tiles = []
        self.create_random_tile()

    def create_random_tile(self):
        number = random.randint(1, 6)
        if number == 1:
            new_tile = Turtle("square")
            new_tile.color(random.choice(COLOR_LIST))
            new_tile.penup()
            new_tile.shapesize(2, 1)
            new_tile.setheading(90)
            new_tile.goto(400, random.randint(-240, 240))
            self.random_tiles.append(new_tile)

    def move_each_tile(self):
        for tile in self.random_tiles:
            tile.goto(tile.xcor() - 15, tile.ycor())

    def racer_collide(self, racer):
        check_list = self.random_tiles
        if len(check_list) > 50:
            check_list = check_list[-50:]
        for tile in check_list:
            if tile.distance(racer) <= 20:
                return True

    def reset_tiles(self):
        for tile in self.random_tiles:
            tile.goto(-1000, -1000)
        self.random_tiles = []