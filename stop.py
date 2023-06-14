# Next, create a program stop.py that has the following functions:
# • rectangle: takes the width and height as parameters and draws a rectangle (each interior angle is 90°)
# • octagon: takes the side length as a parameter and draws an octagon (each exterior turn is 45°)
# • stop: takes the octagon side length as a parameter and draws a stop sign by calling octagon, 
# moving forward 3/8 of the side length, and drawing a rectangle sign post that is 1/5 of the side wide 
# and has a height that is double a side.
# Note that your shape functions must use a for loop. 
# Test that your functions are working by drawing multiple stop signs of different sizes. 

import turtle

def rectangle(width, height):
    for i in range(2):
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)

def octogon(length):
  for i in range(8):
    turtle.forward(length)
    turtle.left(45)

def stop(length):
  octogon(length)
  turtle.forward(length*(3/8))
  rectangle(length*(1/5), length*2)
  
stop(50)
back(200)
stop(25)

turtle.Screen().exitonclick()