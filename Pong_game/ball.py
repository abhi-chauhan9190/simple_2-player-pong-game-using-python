from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('red')
        self.penup()
        self.x_move=8
        self.y_move=8
        self.movespeed=0.1
    def move(self):
        nx=self.xcor() + self.x_move
        ny=self.ycor() + self.y_move
        self.goto(nx,ny)
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1 
        self.movespeed *= 0.8 
    def r_position(self):
        self.goto(0,0) 
        self.movespeed=0.1   
        self.bounce_x()  

