import turtle
import random

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)

turtle.penup()

SQUARE_SIZE=20
START_LENGTH=1

score_list=[]
pos_list=[]
stamp_list=[]
food_pos=[]
food_stamp=[]

snake=turtle.clone()
snake.shape("square")
food=turtle.clone()

turtle.hideturtle()

for i in range(START_LENGTH):
    x_pos=snake.pos()[0]
    y_pos=snake.pos()[1]

    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos)
    snake.goto(x_pos,y_pos)

    pos_list.append(my_pos)

    stamp1=snake.stamp()
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



edges=turtle.clone()
edges.pu()
edges.goto(-395,245)
edges.pd()
edges.goto(395,245)
edges.goto(395,-245)
edges.goto(-395,-245)
edges.goto(-395,245)
edges.goto(-395,-245)

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

#food_stamps=[]
#turtle.register_shape("snakefood.gif")
#food=turtle.clone()
#food.shape("snakefood.gif")

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


    
def move_snake():
    global score
    
    my_pos=snake.pos()
    x_pos=my_pos[0]
    y_pos=my_pos[1]

    global direction
     
    

    if direction==RIGHT:
        snake.goto(x_pos+SQUARE_SIZE, y_pos)
        #print("you moved right")
    elif direction==LEFT:
        snake.goto(x_pos-SQUARE_SIZE, y_pos)
        #print("you moved left")
        
    if direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        #print("you moved UP")
    if direction==DOWN:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
       # print("you moved down")


    my_pos=snake.pos()
    pos_list.append(my_pos)
    new_stamp=snake.stamp()
    stamp_list.append(new_stamp)

    if snake.pos() in pos_list[0:-1]:
        quit()
    
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        turtle.clear()
        score=score+1
        score_list.append(score)
        turtle.write('score='+str(score))
        
        
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you have eaten the food!")
        make_food()
        

        stamp_list.append(stamp1)
        pos_list.append(stamp1)

    old_stamp=stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)


    new_pos=snake.pos()
    new_x_pos=new_pos[0]
    new_y_pos=new_pos[1]

    if new_x_pos>=RIGHT_EDGE:
        print("you hit the right edge! GaMe OVeR")
        quit()
    if new_x_pos<=LEFT_EDGE:
        print("you hit the left edge! GaMe OVeR")
        quit()
    if new_y_pos>=UP_EDGE:
        print("you hit the upper edge! GaMe OVeR")
        quit()
    if new_y_pos<=DOWN_EDGE:
        print("you hit the lower edge! GaMe OVeR")
        quit()
    
        
    turtle.ontimer(move_snake,TIME_STEP)

move_snake()
make_food()
