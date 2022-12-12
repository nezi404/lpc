# Libraries for graphic plotting and for math usage needs
import turtle
import math


# Square drawing function
def fibonacci_plotting(iteration_number):
    a = 0
    b = 1
    square_one = a
    square_two = b

    # Turning the pen for squares blue
    the_pen.pencolor("blue")

    # Drawing the first square of 1 x 1
    the_pen.fd(b * factor)
    the_pen.lt(90)
    the_pen.fd(b * factor)
    the_pen.lt(90)
    the_pen.fd(b * factor)
    the_pen.lt(90)
    the_pen.fd(b * factor)

    # Fibonacci application for the rest of the squares
    temporary_length = square_two
    square_two = square_two + square_one
    square_one = temporary_length

    # Upcoming new unknown square unities drawings
    for lines in range(1, iteration_number):
        the_pen.backward(square_one * factor)
        the_pen.rt(90)
        the_pen.fd(square_two * factor)
        the_pen.lt(90)
        the_pen.fd(square_two * factor)
        the_pen.lt(90)
        the_pen.fd(square_two * factor)

        # Fibonacci theory for the rest of the squares(continuation)
        temporary_length = square_two
        square_two = square_two + square_one
        square_one = temporary_length

    # After drawing all the squares we set the pen for drawing the
    # spiral line
    the_pen.penup()
    # Bring it back to the origin
    the_pen.setpos(factor, 0)
    the_pen.seth(0)
    the_pen.pendown()

    # Turning the colour of the pen for spiral plotting to red for
    # a better understanding of the graphic
    the_pen.color("red")

    # Drawing the Fibonacci spiral plotting
    the_pen.lt(90)
    for i in range(iteration_number):
        print(b)
        spiral = math.pi * b * factor/2
        spiral = spiral/90
        for j in range(90):
            the_pen.fd(spiral)
            the_pen.lt(1)
        temporary_length = a
        a = b
        b = temporary_length + b


factor = 1

# Asking the user the desired number of iteration
iteration_number = int(input("Enter the number of iterations, (must be > 1): "))
if iteration_number > 0:
    print(f"Fibonacci series for {iteration_number} elements: ")
    the_pen = turtle.Turtle()
    the_pen.speed(100)
    fibonacci_plotting(iteration_number)
    turtle.done()
else:
    # Since it is not possible to have a zero in Fibonacci theory, this
    #  error message will display
    print("Number of iterations must be > 0")
    
