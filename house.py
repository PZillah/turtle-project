# Step 7. Draw a picture with functions
# Create a program house.py that has the following functions:
# • square: takes the length of a side as a parameter and draws a square (each
# interior angle is 90°)
# • triangle: takes the length of a side as a parameter and draws an equilateral
# triangle (each exterior turn is 120°)
# • house: takes the length of
# a line as a parameter and draws a house by calling your triangle and square functions.
# Make sure that your square and triangle functions use a for loop.
# Test that your functions are working by drawing multiple houses of different sizes. 

import turtle

#helper function
def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()
  
def square(size):
  for i in range(4):
    turtle.forward(size)
    turtle.right(90)

def triangle(size):
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)

def house(length):
  square(length)
  triangle(length)
  
house(100)
back(100)
house(50)


turtle.Screen().exitonclick()
