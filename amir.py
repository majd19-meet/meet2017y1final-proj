print('choose your player')
print('adam, doudou, amir, kayvon, jan, alex')

fatman=turtle.clone()
fatman.penup()
turtle.register_shape('adam.gif')
turtle.register_shape('dou_dou.gif')
turtle.register_shape('amir.gif')
turtle.register_shape('kayvon.gif')
turtle.register_shape('jan.gif')
turtle.register_shape('alex.gif')

if chose=='adam':
    fatman.shape('adam.gif')
elif chose=='doudou':
    fatman.shape('dou_dou.gif')
elif chose=='amir':
    fatman.shape('amir.gif')
elif chose=='kayvon':
    fatman.shape('kayvon.gif')
elif chose=='jan':
    fatman.shape('jan.gif')
elif chose=='alex':
    fatman.shape('alex.gif')
    
