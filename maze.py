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
for i in range (4):
    turtle.goto(x_pos,y_pos)
    x_pos-=20
    turtle.stamp()
for i in range (10):
    turtle.goto(x_pos,y_pos)
    y_pos+=20
    turtle.stamp()
for i in range (4):
    turtle.goto(x_pos,y_pos)
    x_pos+=20
    turtle.stamp()
for i in range (10):
    turtle.goto(x_pos,y_pos)
    y_pos-=20
    turtle.stamp()


x_pos = 380
y_pos = -230


for i in range (23):
    turtle.goto(x_pos,y_pos)
    y_pos+=20
    turtle.stamp()


for i in range (38):
    turtle.goto(x_pos,y_pos)
    x_pos-=20
    turtle.stamp()

for i in range (23):
    turtle.goto(x_pos,y_pos)
    y_pos-=20
    turtle.stamp()

for i in range (38):
    turtle.goto(x_pos,y_pos)
    x_pos+=20
    turtle.stamp()

