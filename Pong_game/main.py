from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
sc = Screen()

sc.setup(800,600)
sc.bgcolor("black")
sc.title("2 player Pong Game")
sc.tracer(0)
t1 = Turtle()
pdr = Paddle(350,0)
pdl = Paddle(-350,0)
bl= Ball()
scr = Score()
sc.listen()
t1.color('white')

sc.onkey(pdr.goup,"Up")
sc.onkey(pdr.godown,"Down")
sc.onkey(pdl.goup,"w")
sc.onkey(pdl.godown,"s")
game_is_on=1
while(game_is_on):
    sc.update()
    time.sleep(bl.movespeed)
    bl.move()
    if bl.ycor() > 280 or bl.ycor() < -280:
        bl.bounce_y()
        
    if bl.distance(pdr) < 50 and bl.xcor() > 320 or bl.distance(pdl) < 50 and bl.xcor() < -320 :
        bl.bounce_x()
    if bl.xcor() > 380:
        bl.r_position() 
        scr.lpoint()   
        bl.x_move+=1
        bl.y_move+=1
    if bl.xcor() < -380:
        bl.r_position()  
        scr.rpoint()
        bl.x_move+=1
        bl.y_move+=1
    if scr.lscore == 15 or scr.rscore== 15:
        t1.write("Game Over !!!")   
        game_is_on=0 
        

sc.exitonclick()

