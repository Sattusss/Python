from turtle import *
speed('slowest')
bgcolor('black')
pencolor('red')
penup()
setpos(-200,200)
pendown()
for i in range(50,0,-3):
    forward(i)
    left(90)

speed('slowest')
bgcolor('black')
pencolor('red')
penup()
setpos(200,-200)
pendown()
for i in range(50,0,-3):
    forward(i)
    left(90)

speed('slowest')
bgcolor('black')
pencolor('yellow')
penup()
setpos(200,200)
pendown()
for i in range(50,0,-3):
    forward(i)
    left(90)

speed('slowest')
bgcolor('black')
pencolor('white')
penup()
setpos(-200,-200)
pendown()
for i in range(50,0,-3):
    forward(i)
    left(90)

  
    
mainloop()