import turtle

print('choose your player')
print('adam,dou_dou,kayvon,jan,alex')
chosen=input()
chosen.lower()
register_shape=[]

if chosen=='adam':
    register_shape('adam.gif')

elif chosen=='dou_dou':
    register_shape('dou_dou.gif')

elif chosen=='kayvon':
    register_shape('kayvon.gif')

elif chosen=='jan':
    register_shape('jan.gif')

elif chosen=='alex':
    register_shape('alex.gif')
    
    
