from turtle import Turtle , Screen

class Paddle(Turtle):
    def __init__(self,corx,cory):
        super().__init__()
        self.color('white')
        self.shape("square")
        self.shapesize(5,1)
        self.penup()      
        self.speed(100)
        self.goto(corx,cory)
    def goup(self):
        ycor=self.ycor()+25
        self.goto(self.xcor(),ycor)
    def godown(self):  
        ycor=self.ycor() - 25
        self.goto(self.xcor(),ycor)    

    