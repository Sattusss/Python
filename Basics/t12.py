from turtle import *
speed('fastest')
s = Screen()
s.setup(1000,700)
colors = ['yellow','green','red','blue']
pencolor('purple')
pensize(5)
for i in range(10,0,-1):
    penup()
    setpos(0,-20*i)
    pendown()
    fillcolor(colors[i%4])
    begin_fill()
    circle(20*i)
    end_fill()
mainloop()
