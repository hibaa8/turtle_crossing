from turtle import Turtle
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.x = 0
        self.y = -270
        self.goto(self.x, self.y)
        self.setheading(90)

    def up(self):
        self.y += 10
        self.forward(10)

    def down(self):
        if self.y >= -270:
            self.y -= 10
            self.backward(10)

    def reset(self):
        self.goto(0,-275)
