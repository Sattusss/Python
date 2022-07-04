from ast import Import
from pkgutil import ImpImporter
from turtle import *
speed(0)
bgcolor('yellow')
pencolor('red')
i = 5
while True:
    circle(i,i)
    forward(i)
    left(60)
    i += 5
    if i > 500:
        break