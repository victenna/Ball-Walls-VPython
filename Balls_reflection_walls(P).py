import turtle,random,time
wn=turtle.Screen()
wn.setup(900,700)
wn.bgcolor('black')
turtle.tracer(7)
ball=[]
X=[]
Y=[]
dx=[]
dy=[]
count=6
wn.addshape('wall1.gif')
plate1=turtle.Turtle()
plate1.shape('wall1.gif')
plate1.up()
plate1.goto(0,250)


wn.addshape('wall2.gif')
plate2=turtle.Turtle()
plate2.shape('wall2.gif')
plate2.up()
plate2.goto(0,-250)

sphere=['ballred.gif','ballwhite.gif','ballgold.gif',\
     'ballviolet.gif','ballgreen.gif','ballblue.gif']
ball=[]
for i in range(6):
    wn.addshape(sphere[i])
    ball.append(turtle.Turtle())
    ball[i].shape(sphere[i])
   
for i in range(count):
    ball[i].up()
    ball[i].hideturtle()
    ball[i].setposition(random.randint(-100,100),\
                        random.randint(200,255))
    dx.append(random.randint(-2,2))
    dy.append(-50)
    
              
    X.append(ball[i].xcor())
    Y.append(ball[i].ycor())
    ball[i].showturtle()
turtle.tracer(2)


while True:
    for n in range(count):
        ball[n].setposition(X[n]+dx[n],Y[n]+dy[n])
        X[n]=ball[n].xcor()
        Y[n]=ball[n].ycor()
        time.sleep(0.01)
        if Y[n]<-210 or Y[n]>210:
            dy[n]=-dy[n]
           
                              

