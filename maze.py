import turtle
SIZE_X=800
SIZE_Y=500
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
left_corner=(-385,-240)
wall_maker(left_corner,25,35)
left_corner=(-50,-50)
wall_maker(left_corner,15,5)
