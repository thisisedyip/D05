#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit
import sys

# Body


def infinite_stairway_room(count=0):
    print(sys.argv[1]+" walks through the door to see a dimly lit hallway.")
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("Do you want to 'take stairs' or 'go back': ")
    
    # infinite stairs option
    if next == "take stairs":
        print(sys.argv[1] + ' takes the stairs')
        if (count > 0):
            print("but "+ sys.argv[1] + "is not happy about it")
        infinite_stairway_room(count + 1)
    # option 2 == ?????
    elif next == 'go':
        cthulhu_room()
    elif next == 'back':
        backroom()
        pass


def gold_room():
    print("This room is full of gold.  How much do you take, "+ sys.argv[1] + "?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win, "+ sys.argv[1] + "!")
        exit(0)
    else:
        dead("You greedy goose! You dead, " + sys.argv[1] + "!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear, " + sys.argv[1] + "?")
    bear_moved = False

    while True:
        next = str(input("Do you want to take the honey, taunt the bear, or open the door? \n> "))

        if next == "take" or next == "honey":
            dead("The bear looks at you then slaps your face off, " + sys.argv[1] + ".")
        elif next == "taunt" and not bear_moved:
            print("The bear has moved from the door. You can go through it now, " + sys.argv[1] + ".")
            bear_moved = True
        elif next == "taunt" and bear_moved == True:
            dead("The bear gets pissed off and chews your leg off, " + sys.argv[1] + ".")
        elif (next == "open" or next == "door") and bear_moved:
            gold_room()
        elif (next == "open" or next == "door") and not bear_moved:
            print("You can't open the door, " + sys.argv[1] + ".  The bear is in front of it.")
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you, " + sys.argv[1] + ", see the great evil Cthulhu.")
    print("He, it, whatever stares at you, " + sys.argv[1] + " and you go insane.")
    print("Do you, " + sys.argv[1] + " flee for your life or let it eat your head?")

    next = input("> ")

    if "flee" in next:
        infinite_stairway_room()
    elif "head" in next:
        dead("Well that was tasty!")
    elif "back" in next:
        backroom()
    else:
        cthulhu_room()

def backroom():
    print("Surprise!  You've discovered the backroom filled with awesome programmers.")
    username = str(input("Please state your name: "))
    print("Welcome to the guild of programmers, " + username + ".  You are home now and will never leave...")
    exit(0)

def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    print("Hello there, " + sys.argv[1] + ".")
    print("You are in a dark room, " + sys.argv[1] + ".")
    print("There is a door to your right and left, " + sys.argv[1] + ".")
    print("Which one do you take, " + sys.argv[1] + "?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve, " + sys.argv[1] + ".")

if __name__ == '__main__':
    main()
