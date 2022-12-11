# Libraries: turtle for graphics and random for built-in functions
import turtle
import random

""" Two players are able to play the game but,firstly, we make the 
player one and after a clone for player two, giving it a different 
colour and initial position.
"""
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200, 100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200, -100)

# Making the finish line for each player
# and taking them back to the start
player_one.goto(300, 60)
player_one.pendown()
# The finish line of each player will be a circle
player_one.circle(40)
player_one.penup()
player_one.goto(-200, 100)
player_two.goto(300, -140)
player_one.pendown()
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200, -100)
player_two.pendown()

# Making a die with the usage of a list
die = [1, 2, 3, 4, 5, 6]

# Starting the process of the game, with a loop of 20, which would be
# the minimum for any player to win a match
for rounds in range(20):
    #  if any player hasn't reached any of the respective coordinates
    # the game will continue until it is reached by rolling the die

    if player_one.pos() >= (300, 100):
        print("Player One Wins!")

        break

    if player_two.pos() >= (300, -100):
        print("Player Two Wins!")

        break

    else:

        # Both player gets to roll the dice and make their
        #  own turtle move to the coordinate given by the die
        player_one_turn = input("Press 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_one.fd(die_outcome*20)
        player_two_turn = input("Press 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20 * die_outcome)
        player_two.fd(20*die_outcome)
