#Today we’ll use python’s turtle module to draw shapes using loops, functions, and variables to draw pictures.

import turtle

#step 1. Draw a line

# turtle.shape("turtle") # optional
# turtle.speed(0) # optional
# turtle.forward(90) #move foward
# turtle.left(90) #rotate left 90 degrees
# turtle.forward(90)
############################################################
#step 2. Draw a square
# 1. Draw a square on the screen.
# 2. Change its color.
# 3. Make the line thicker by changing the pensize or width.
# 4. Change the speed the turtle draws.

# turtle.shape("turtle")
# turtle.color("green")
# turtle.width(5)
# turtle.speed(10) 
# for i in range(4):
#   turtle.forward(90) 
#   turtle.left(90)
############################################################
# Step 3. Draw two squares
# It’s possible to move the turtle without drawing.
# Draw two squares on the screen that don’t touch.
# See the example on the right. To speed up
# testing, set the turtle speed to be 0.

#helper function
# def back(len):
#   turtle.penup()
#   turtle.backward(len)
#   turtle.pendown()
  
# turtle.shape("turtle")
# turtle.color("green")
# turtle.width(5)
# turtle.speed(10) 

# for i in range(2):
#   for j in range(4):
#     turtle.forward(90) 
#     turtle.left(90)
#   back(100)

############################################################
