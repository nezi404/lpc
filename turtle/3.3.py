import turtle


# Function for showing the screen
display = turtle.Screen()
# Creating the "pen" for the triangles drawings
the_pen = turtle.Turtle()

# Function that draws the triangles
def draw_triangle(coordinate_x, coordinate_y):
    # To make the pen be able to move around without leaving traces
    the_pen.penup()
    # Moving the pen to the cursor coordinates
    the_pen.goto(coordinate_x, coordinate_y)
    # Making the pen "draw" again
    the_pen.pendown()
 
    # Drawing each stroke of the triangle half by half in three times
    for sides in range(3):
        # Drawing the half of the triangle's side
        the_pen.fd(100)
        # Changing the direction of the "pen"
        the_pen.lt(120)
        # Drawing the half of the triangle's side
        the_pen.fd(100)

# Built-in function that reads where is/was the cursor
# click on the window
turtle.onscreenclick(draw_triangle, 1)
# Function that checks if there are any connection
turtle.listen()
# Function that keep the screen window on
turtle.done()
