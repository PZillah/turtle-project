#turtle party by Priscilla
#6/12/23
#run on trinket.io/turtle

import turtle #turtle module from python

turtle.color("teal")

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

def triangle(size):
  for i in range(3):
    turtle.forward(size)
    turtle.left(120)
    
def square(size):
  for i in range(4):
    turtle.forward(size)
    turtle.left(90)

def polygon(numOfSides, size):
  for i in range(numOfSides):
    turtle.forward(size)
    turtle.left(360 / numOfSides)
    
def spiral(len, angle):
  for i in range(len, 5, -5):
    turtle.forward(i)
    turtle.left(angle)


spiral(100, 90)
# for n in range(3, 5):
#   polygon(3, 50)
#   turtle.left(60)
  
#polygon(4, 100)
# triangle(100)
# back(75)
# triangle(50)
# back(50)
# triangle(25)
# square(100)
# back(75)
# square(50)
# back(50)
# square(25)





