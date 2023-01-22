from turtle import Screen
from random_tiles import RandomTile
from racer import Racer
from level import Level
import time

def next_level():
    racer.reset_racer_position()
    level.update_level()
    return sleep_time * 0.92

def restart_game():
    screen.tracer(0)
    level.game_over()
    screen.update()
    time.sleep(1)
    level.update_highest_score()
    tile.reset_tiles()
    racer.reset_racer_position()
    return 0.1

screen = Screen()
screen.tracer(0)
tile = RandomTile()
racer = Racer()
level = Level()
racer.move_race(screen)
screen.setup(800, 600)
screen.title("TURTLE CROSSING")
screen.bgcolor("black")
sleep_time = 0.1
col = 1
while True:
    screen.update()
    tile.create_random_tile()
    tile.move_each_tile()
    if racer.ycor() > 280:
        sleep_time = next_level()
    if tile.racer_collide(racer):
        sleep_time = restart_game()
    time.sleep(sleep_time)

screen.exitonclick()
