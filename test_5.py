
import turtle

size = int(input("Enter size: "))
color = input("Enter color: ")

shape = turtle.Turtle()
shape.shape("turtle")
shape.color(color)

for _ in range(4):
    shape.forward(size)
    shape.left(90)
    shape.forward(size)
    shape.left(90)
   
turtle.mainloop()
