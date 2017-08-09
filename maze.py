import turtle
x_pos=0
y_pos=0


wall_pos=[]
box=turtle.clone()
box.shape('square')
box.hideturtle()
box.penup()
SQUARE_SIZE=20

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







#left_corner=(260,-110)
#width=12
#hight=9
#for i in range (5):
    #3x=left_corner[0]
    #y=left_corner[1#
    #left_corner=(x+20,y+20)
    #width += -2
    #hight += -2
    #wall_maker(left_corner,hight,width)

