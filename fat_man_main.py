
import turtle
import random

turtle.tracer(1,0)

SIZE_X=1250
SIZE_Y=700

turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()


UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100
SPACEBAR='space'
global score
UP=0
DOWN=1
LEFT=2
RIGHT=3


direction=UP
direction=0
score=0
def up():
    global direction
    if direction != DOWN:
        direction=UP
    #print("You pressed the up key!")

def down():
    global direction
    if direction !=UP:

        direction=DOWN
    #print("You pressed the down key!")

def left():
    global direction
    if direction!=RIGHT:
        direction=LEFT
    #print("You pressed the left key!")

def right():
    global direction
    if direction!=LEFT:
        direction=RIGHT
    #print("You pressed the right key!")


turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

food_stamps=[]
food=turtle.clone()
food.shape("square")



#lists
pos_list=[]
stamp_list=[]
score_list=[]
player_list=[]
food_pos=[]

#turtles
food=turtle.clone()
fat_man=turtle.clone()
#shape
fat_man.shape("square")
#lists
pos_list=[]
stamp_list=[]
score_list=[]
player_list=[]
food_pos=[]

