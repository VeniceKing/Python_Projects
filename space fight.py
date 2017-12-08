# -*- coding: utf-8 -*-

# Created on Thu Nov  9 11:26:31 2017

# @author: Jordy

# The game will let you shoot 3 aliens.
# Each alien killed will net you certain amount points.
# If the player gets 100 points, they win!
# Killing humans looses you points!


from random import randint

space = ["A", "A", "A", "A", "A", "A", "A"]
score = 0

def start():
    print("Welcome to Space Fight")
    print(space)

# Board create method

def board_create():
    global alien_1
    alien_1 = randint(1,7)
    print("Game Initialized")
    #Debug
    print(alien_1)

def shoot():
# This creates number of turns
    for x in range(1, 4):
        shot = input("shoot where?")
        if int(shot) == alien_1:
            space[int(shot) - 1] = "%"
            print("You hit an alien!")
            global score 
            score += 60
            print("Score is " + str(score))
            print(space)
        else:
            space[int(shot)] = "-"
            print("You hit empty space!")
            print(space)
    print("Congratulations Your Final Score is " + str(score))

# Call functions here
start()
board_create()
shoot()