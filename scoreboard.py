from turtle import Turtle
from time import sleep
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.level = 1
        self.num_lives()
        self.update_scoreboard()

    def num_lives(self):
        if self.level in (1,2):
            self.lives = 3
        elif self.level in (3,4):
            self.lives = 2
        elif self.level in (5,6):
            self.lives = 1

    def update_scoreboard(self):
        self.clear()
        self.goto(185, 270)
        self.write(f'Lives:{self.lives}', font=FONT)
        self.goto(-290,270)
        self.write(f'Level:{self.level}', font=FONT)

    def increment(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write('Game Over', align='center', font=FONT)

    def reset(self):
        self.home()
        self.write('Level up!', align='center', font=FONT)
        sleep(1)
        self.level += 1
        self.num_lives()
        self.update_scoreboard()
