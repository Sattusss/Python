import pgzrun
HEIGHT = 500
WIDTH = 500
box = Rect(50,50,100,130)
box2 = Rect(250,50,100,250)
box3 = Rect((400,400),(10,100))
def draw():
    screen.fill('Black')
    screen.draw.rect(box,'red')
    screen.draw.filled_rect(box2,'yellow')
    screen.draw.filled_rect(box3,'White')
    screen.draw.text('These are Rectangles',(70,300),color='green')
pgzrun.go()