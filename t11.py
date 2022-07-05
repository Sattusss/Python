from turtle import *
pencolor('blue')
pensize(3)
fillcolor('yellow')
speed('fastest')
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    lt(27)
    end_fill()
goto(20,250)
mainloop()