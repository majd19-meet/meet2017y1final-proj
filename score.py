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


direction=0
def up():
    global direction
    direction=UP
    score = 0
    #print("You pressed the up key!")

def down():
    global direction
    direction=DOWN
    score = 0
    #print("You pressed the down key!")

def left():
    global direction
    direction=LEFT
    score = 0
    #print("You pressed the left key!")

def right():
    global direction
    direction=RIGHT
    score = 0
    #print("You pressed the right key!")

def move_fatman():
    global score

if fatman.pos() in food_pos:
        food_ind=food_pos.index(fatman.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        score=0
        score = score+1
        score_list.append(score)
        turtle.write('score='+str(score))
        print('you have eaten the food')
        make_food()
