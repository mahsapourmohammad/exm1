import turtle as t
from time import sleep

wn=t.Screen()
wn.setup(600,500)
wn.bgcolor('black')

obj=t.Turtle()
obj.ht()
obj.width(3)
obj.direction='stop'


def go_up():
    obj.direction='up'

def go_down():
    obj.direction='down'

def go_right():
    obj.direction='right'

def go_left():
    obj.direction='left'

def move():
    if obj.direction=='up':
        y=obj.ycor()
        obj.sety(y+30)

    if obj.direction=='down':
        y=obj.ycor()
        obj.sety(y-30)

    if obj.direction=='right':
        y=obj.xcor()
        obj.setx(y+30)

    if obj.direction=='left':
        y=obj.xcor()
        obj.setx(y-30)

wn.listen()

wn.onkeypress(go_up,'u')

wn.onkeypress(go_down,'d')

wn.onkeypress(go_right,'r')


wn.onkeypress(go_left,'l')


while True:
    wn.update()
    move()
    sleep(0.1)
    wn.mainloop()