import turtle
import random

##HEAD
print('choose your player')
print('adam, doudou, kayvon,jan,alex')
chose=input()
chose.lower()


fatman=turtle.clone()
chosen=turtle.clone()

turtle.register_shape('adam.gif')
turtle.register_shape('dou_dou.gif')
turtle.register_shape('kayvon.gif')
turtle.register_shape('jan.gif')
turtle.register_shape('alex.gif')



if chose=='adam':
    chosen.shape('adam.gif')
elif chose=='doudou':
    chosen.shape('dou_dou.gif')
elif chose=='kayvon':
    chosen.shape('kayvon.gif')
elif chose=='jan':
    chosen.shape('jan.gif')
elif chose=='alex':
    chosen.shape('alex.gif')
    
    




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
food_pos=[]
food_stamp=[]

fatman=turtle.clone()
#fatman.shape(chosen)

turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos=fatman.pos()[0]
    y_pos=fatman.pos()[1]

    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    fatman.goto(x_pos,y_pos)

    pos_list.append(my_pos)

    stamp1=fatman.stamp()
    stamp_list.append(stamp1)

START_LENGTH=1
for i in range (START_LENGTH):
    x_pos=fatman.pos()[0]
    y_pos=fatman.pos()[1]
    x_pos= x_pos+SQUARE_SIZE
    new_pos=(x_pos,y_pos)
    fatman.goto (x_pos,y_pos)
    pos_list.append(new_pos)

    stamp1 = fatman.stamp
    stamp_list.append(stamp1)



UP_ARROW="Up"
LEFT_ARROW="Left"
DOWN_ARROW="Down"
RIGHT_ARROW="Right"
TIME_STEP=100
SPACEBAR='space'
global score
score=0
UP=0
DOWN=1
LEFT=2
RIGHT=3

def move_fatman():
    if direction==RIGHT:
        new_pos=(x_pos+SQUARE_SIZE,y.pos)
        if new_pos in wall_pos:
            turtle.ontimer(move_fatman,timestep)
        else:
            snake.goto(new_pos)

    if direction==LEFT:
        new_pos=(x_pos-SQUARE_SIZE,y.pos)
        if new_pos in wall_pos:
            turtle.ontimer(move_fatman,timestep)
        else:
            snake.goto(new_pos)

    if direction==UP:
        new_pos=(x_pos,y.pos+SQUARE_SIZE)
        if new_pos in wall_pos:
            turtle.ontimer(move_fatman,timestep)
        else:
            snake.goto(new_pos)

    if direction==DOWN:
        new_pos=(x_pos,y.pos-SQUARE_SIZE)
        if new_pos in wall_pos:
            turtle.ontimer(move_fatman,timestep)
        else:
            snake.goto(new_pos)




UP_EDGE=SIZE_Y/2
DOWN_EDGE=-SIZE_Y/2
RIGHT_EDGE=SIZE_X/2
LEFT_EDGE=-SIZE_X/2


direction=0
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


def move_fatman():
    global score

    my_pos=fatman.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]
    global direction

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




    global food_stamp, food_pos
    if fatman.pos() in food_pos:
        food_ind=food_pos.index(fatman.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print('you have eaten the food')
        make_food()

    else:
        old_stamp=stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)



        turtle.ontimer(move_fatman, TIME_STEP)

move_fatman()

food_pos=[(100,100)]
food_stamps=[]

for i in food_pos:
    food.goto(i)
    food_stamp=food.stamp()
    food_stamps.append(food_stamps)
        
