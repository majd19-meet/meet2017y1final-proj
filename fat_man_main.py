import turtle
import random

turtle.tracer(1,0)

SIZE_X=1250
SIZE_Y=700
turtle.setup(SIZE_X,SIZE_Y)

turtle.penup()

SQUARE_SIZE=20
START_LENGTH=1

score_list=[]
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamp=[]
#wadi's part
fat_man=turtle.clone()
#fat_man.shape(chosen)

turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos=fat_man.pos()[0]
    y_pos=fat_man.pos()[1]

    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    fat_man.goto(x_pos,y_pos)

    pos_list.append(my_pos)

    stamp1=fat_man.stamp()
    stamp_list.append(stamp1)

START_LENGTH=1
for i in range (START_LENGTH):
    x_pos=fat_man.pos()[0]
    y_pos=fat_man.pos()[1]
    x_pos= x_pos+SQUARE_SIZE
    new_pos=(x_pos,y_pos)
    fat_man.goto (x_pos,y_pos)
    pos_list.append(new_pos)

    stamp1 = fat_man.stamp
    stamp_list.append(stamp1)






 
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
UP_EDGE=SIZE_Y/2
DOWN_EDGE=-SIZE_Y/2
RIGHT_EDGE=SIZE_X/2
LEFT_EDGE=-SIZE_X/2

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

def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1

    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food.pos=(food_x,food_y)
    food_pos.append(food.pos)
    ran_food_stamp=food.stamp()
    food_stamps.append(ran_food_stamp)


def move_fat_man():
    global score

    my_pos=fat_man.pos
