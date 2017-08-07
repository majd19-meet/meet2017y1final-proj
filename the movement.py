import turtle
import random


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
