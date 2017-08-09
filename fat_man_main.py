import turtle
import random

##HEAD
print('choose your player')
print('adam, doudou, kayvon,jan,alex')
chose=input()
chose.lower()

fatman=turtle.clone()
fatman.penup()
turtle.register_shape('adam.gif')
turtle.register_shape('dou_dou.gif')
turtle.register_shape('kayvon.gif')
turtle.register_shape('jan.gif')
turtle.register_shape('alex.gif')



if chose=='adam':
    fatman.shape('adam.gif')
elif chose=='doudou':
    fatman.shape('dou_dou.gif')
elif chose=='kayvon':
    fatman.shape('kayvon.gif')
elif chose=='jan':
    fatman.shape('jan.gif')
elif chose=='alex':
    fatman.shape('alex.gif')
    
    




###af566edc26b76e655e984c42088f41b0e475851e

    
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


turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos=fatman.pos()[0]
    y_pos=fatman.pos()[1]

    my_pos=(x_pos,y_pos)

    pos_list.append(my_pos)

    stamp1=fatman.stamp()
    stamp_list.append(stamp1)


UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100
SPACEBAR='space'
score=0
UP=0
DOWN=1
LEFT=2
RIGHT=3

##def move_fatman():
##    if direction==RIGHT:
##        new_pos=(x_pos+SQUARE_SIZE,y.pos)
##        if new_pos in wall_pos:
##            turtle.ontimer(move_fatman,timestep)
##        else:
##            fatman.goto(new_pos)
##
##    if direction==LEFT:
##        new_pos=(x_pos-SQUARE_SIZE,y.pos)
##        if new_pos in wall_pos:
##            turtle.ontimer(move_fatman,timestep)
##        else:
##            fatman.goto(new_pos)
##
##    if direction==UP:
##        new_pos=(x_pos,y.pos+SQUARE_SIZE)
##        if new_pos in wall_pos:
##            turtle.ontimer(move_fatman,timestep)
##        else:
##            fatman.goto(new_pos)
##
##    if direction==DOWN:
##        new_pos=(x_pos,y.pos-SQUARE_SIZE)
##        if new_pos in wall_pos:
##            turtle.ontimer(move_fatman,timestep)
##        else:
##            fatman.goto(new_pos)
##


wall_pos=[]
box=turtle.clone()
box.shape('square')
box.hideturtle()
box.penup()


#wall maker
def wall_maker (left_corner,hight,width):
    box.goto(left_corner[0],left_corner[1]-SQUARE_SIZE)

    for i in range(hight):
        box.goto(box.pos()[0],box.pos()[1]+SQUARE_SIZE)
        box.stamp()
        wall_pos.append(box.pos)


    for i in range(width-1):
        box.goto(box.pos()[0]+SQUARE_SIZE,box.pos()[1])
        box.stamp()
        wall_pos.append(box.pos())
    for i in range (hight-1):
        box.goto(box.pos()[0],box.pos()[1]-SQUARE_SIZE)
        box.stamp()
        wall_pos.append(box.pos())
    for i in range(width-2):
        box.goto(box.pos()[0]-SQUARE_SIZE,box.pos()[1])
        box.stamp()
        wall_pos.append(box.pos())
    

        
left_corner=(-608,-337)
wall_maker(left_corner,35,62)
#maze

left_corner=(-460,-260)

width=12
hight=13
for i in range (5):
    x=left_corner[0]
    y=left_corner[1]
    left_corner=(x+20,y+20)
    width += -2
    hight += -2
    wall_maker(left_corner,hight,width)
    
    

left_corner=(-460,45)
width=12
hight=13
for i in range (5):
    x=left_corner[0]
    y=left_corner[1]
    left_corner=(x+20,y+20)
    width += -2
    hight += -2
    wall_maker(left_corner,hight,width)

left_corner=(260,-260)
width=12
hight=13
for i in range (5):
    x=left_corner[0]
    y=left_corner[1]
    left_corner=(x+20,y+20)
    width += -2
    hight += -2
    wall_maker(left_corner,hight,width)


left_corner=(260,45)
width=12
hight=13
for i in range (5):
    x=left_corner[0]
    y=left_corner[1]
    left_corner=(x+20,y+20)
    width += -2
    hight += -2
    wall_maker(left_corner,hight,width)



UP_EDGE=SIZE_Y/2
DOWN_EDGE=-SIZE_Y/2
RIGHT_EDGE=SIZE_X/2
LEFT_EDGE=-SIZE_X/2


direction=0
def up():
    global direction
    direction=UP
    #print("You pressed the up key!")

def down():
    global direction
    direction=DOWN
    #print("You pressed the down key!")

def left():
    global direction
    direction=LEFT
    #print("You pressed the left key!")

def right():
    global direction
    direction=RIGHT
    #print("You pressed the right key!")

turtle.onkeypress(up,UP_ARROW)
turtle.onkeypress(down,DOWN_ARROW)
turtle.onkeypress(left,LEFT_ARROW)
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()

food=turtle.clone()
food.shape("square")

food_pos=[(100,100)]
food_stamps=[]

for i in food_pos:
    food.goto(i)
    food_stamp=food.stamp()
    food_stamps.append(food_stamp)


def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+2
    max_x=int(SIZE_X/2/SQUARE_SIZE)-2
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+2
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-2
    
    food_x=random.randint(min_x,max_x)*SQUARE_SIZE
    food_y=random.randint(min_y,max_y)*SQUARE_SIZE
    temp_pos= (food_x,food_y)
    if temp_pos in wall_pos:
        make_food()
    else:
        food.goto(food_x,food_y)
        food_pos.append((food_x,food_y))
        ran_food_stamp=food.stamp()
        food_stamps.append(ran_food_stamp)



def move_fatman():
    global score

    my_pos=fatman.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]

    if direction==RIGHT:
        fatman.goto(x_pos+SQUARE_SIZE, y_pos)
        #print("you moved right")
    elif direction==LEFT:
        fatman.goto(x_pos-SQUARE_SIZE, y_pos)
        #print("you moved left")
        
    if direction==UP:
        fatman.goto(x_pos,y_pos+SQUARE_SIZE)
        #print("you moved UP")
    if direction==DOWN:
        fatman.goto(x_pos,y_pos-SQUARE_SIZE)
       # print("you moved down")

    my_pos=fatman.pos()
    pos_list.append(my_pos)
    new_stamp=fatman.stamp()
    stamp_list.append(new_stamp)
    old_stamp=stamp_list.pop(0)
    fatman.clearstamp(old_stamp)
    pos_list.pop(0)



    if fatman.pos() in food_pos:
        food_ind=food_pos.index(fatman.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print('you have eaten the food')
        make_food()

    turtle.ontimer(move_fatman, TIME_STEP)

move_fatman()

        





