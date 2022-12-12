# Importing for the visual output
from turtle import *


# Changing the speed of the turtle
speed("fastest")
# Changing the direction of the turtle to go upwards
rt(-90)
# The angle between the main branch and the others
angle = 30


# Function to draw (plot) the branch/branches
def branch_plotting(branch_size, branch_number):

    # The variable branch_size are "sticks" of the tree
    # The variable branch_number is how much
    # "sticks" the tree has in each branch
    if branch_number > 0:
        # Color palette number range
        colormode(255)
        # Making a colour for the "sticks"
        pencolor(0, 255 // branch_number, 0)
        # Drawing the first stroke
        fd(branch_size)
        # Marking the next curvy
        rt(angle)
        # Making the next shorter and how many still lasts
        branch_plotting(0.8 * branch_size, branch_number - 1)
        pencolor(0, 255//branch_number, 0)
        # Changing the angle of the turtle for a new branch
        lt(2 * angle)
        branch_plotting(0.8 * branch_size, branch_number - 1)
        pencolor(0, 255//branch_number, 0)
        rt(angle)
        fd(-branch_size)

# Asking the desired values to the user
values = input("How much big and how many levels? ")
branch_size, branch_number = values.split()
branch_size = int(branch_size)
branch_number = int(branch_number)
branch_plotting(branch_size, branch_number)
