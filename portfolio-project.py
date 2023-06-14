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

# Step 4. Create a square function
# Revise your program to include a square function that takes the length of each side as a
# parameter & draws a square using the turtle. Call this function instead of the lines you
# used to draw the squares in the prior two steps. Using a loop is recommended.

# def square(size):
#   for i in range(4):
#     turtle.shape("turtle")
#     turtle.forward(size)
#     turtle.left(90)
    
# square(50)

############################################################

# Step 5. Create a rectangle function
# Next we are going to generalize our square function by creating a rectangle function
# that takes a width & a height as parameters and uses the turtle to draw a rectangle. 

# def rectangle(width, height):
#   for i in range(2):
#     turtle.shape("turtle")
#     turtle.forward(width)
#     turtle.left(90)
#     turtle.forward(height)
#     turtle.left(90)
    
# rectangle(100,50)

############################################################

# Step 6. Draw a picture
# Using your newly created square & rectangle functions, draw an interesting picture
# using a for loop that calls rectangle and/or square. In your picture, try to include at least
# one rectangle and one square. Your program should not take any user input.

# for i in range(4):
#   rectangle(100,50)
#   turtle.left(45)
#   square(70)
