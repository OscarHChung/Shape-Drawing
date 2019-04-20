from turtle import *
import time

in_play = True
bob = Turtle()

shape = input("What shape would you like me to draw? (Choose between circle, square, and triangle): ")
color = input("What color would you like? ")
size = int(input("How big do you want the shape? (A number between 0-600): "))
bob.color(color)
bob.speed(10)
bob.hideturtle()

if shape == "square":
    bob.penup()
    bob.goto(0-(size/2),0-(size/2))
    bob.pendown()
    bob.begin_fill()
    bob.forward(size)
    bob.left(90)
    bob.forward(size)
    bob.left(90)
    bob.forward(size)
    bob.left(90)
    bob.forward(size)
    bob.end_fill()
    time.sleep(10)

elif shape == "triangle":
    bob.begin_fill()
    bob.forward(size)
    bob.left(120)
    bob.forward(size)
    bob.left(120)
    bob.forward(size)
    bob.end_fill()
    time.sleep(10)

elif shape == "circle":
    bob.penup()
    bob.goto(0,0-size)
    bob.pendown()
    bob.begin_fill()
    bob.circle(size)
    bob.end_fill()
    time.sleep(10)

else:
    print("One of your answers was not valid.")

print("Thanks for playing!")
