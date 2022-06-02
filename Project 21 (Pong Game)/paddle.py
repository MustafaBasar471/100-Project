from turtle import Turtle

class Paddle(Turtle):


    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(position)


    def go_up(self):
        new_y_paddle = self.ycor() + 35
        self.goto(self.xcor(), new_y_paddle)


    def go_down(self):
        new_y_paddle = self.ycor() - 35
        self.goto(self.xcor(), new_y_paddle)