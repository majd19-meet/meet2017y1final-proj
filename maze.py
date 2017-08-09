import turtle
SIZE_X=1250
SIZE_Y=700
turtle.tracer(1,0)
turtle.setup(SIZE_X,SIZE_Y)
turtle.penup()
stamp_list=[]
x_pos=0
y_pos=0

turtle.shape("square")
SQUARE_SIZE=20


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
left_corner=(-460,-220)
wall_maker(left_corner,25,12)
width=12
hight=25
for i in range (5):
    x=left_corner[0]
    y=left_corner[1]
    left_corner=(x+20,y+20)
    width += -2
    hight += -2
    wall_maker(left_corner,hight,width)

left_corner=(260,-220)
width=12
hight=25
for i in range (5):
    x=left_corner[0]
    y=left_corner[1]
    left_corner=(x+20,y+20)
    width += -2
    hight += -2
    wall_maker(left_corner,hight,width)

