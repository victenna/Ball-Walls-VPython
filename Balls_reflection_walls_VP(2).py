from vpython import *


#GlowScript 2.6 VPython 

scene.range = 20   
ball = []  # create a list that will hold all the balls
num = 100  # number of balls

for i in range(num):     # this starts a counting loop
    ball.append(sphere(radius = random()))
    ball[i].color = vector.random()        # useful shortcut here
    ball[i].pos = vec(-1+random(), 0, random())
    ball[i].velocity = 5.0 * vector(-0.5+random(),-5,random()) 
    
    #ball[i].velocity = 5.0 * vector(2*random(),-5,0) 
    ball[i].acc = vec( 0.0, -0.1, 0.0)

floor = box( pos = vec(0,-10,0), size = vec( 50, 0.5, 40),color=color.red )
floor1 = box( pos = vec(0,10,0), size = vec( 50, 0.5, 40),color=color.red )

time = 0.0  
dt = 0.01
   

while True:
        
    rate(1/(5*dt))             
    for i in range(num):     # this starts a counting loop again
        if ( ball[i].pos.y - ball[i].radius < floor.pos.y + 0.5 * floor.size.y):
            ball[i].pos.y = floor.pos.y + ball[i].radius + 0.5 * floor.size.y
            ball[i].velocity.y = - ball[i].velocity.y

        if ( ball[i].pos.y - ball[i].radius > floor1.pos.y + 0.5 * floor1.size.y):
            ball[i].pos.y = floor1.pos.y + ball[i].radius +0.5 * floor1.size.y
            ball[i].velocity.y = - ball[i].velocity.y

        ball[i].pos = ball[i].pos + ball[i].velocity * dt
        ball[i].velocity = ball[i].velocity + ball[i].acc * dt

    time = time + dt

