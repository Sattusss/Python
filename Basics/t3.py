from turtle import *
speed('slowest')
pencolor('red')


sides = 8
for i in range(8):
    forward(75)
    left(360/sides)
    dot(30)
mainloop()