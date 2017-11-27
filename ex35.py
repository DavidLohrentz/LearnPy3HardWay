#!/usr/bin/python3
from sys import exit

def gold_room():
    print("\nThis room is full of gold. How much do you take?")

    choice = input("\n>>> ")

    goldnum = []
    a = ""
    for i in list(choice):
        if i.isdigit():
            goldnum.append(i)
    cooked = a.join(goldnum)
    n = len(cooked)
    if n == 0:
        print("\nInclude a number in your answer, dumbass.")
        gold_room()
    elif int(cooked) < 100:
        print(f"{cooked} is a nice low number. You win.")
        exit(0)
    else:
        dead(f"You greedy bastard. {cooked} is too high for you to win.")

def bear_room():
    print("\nThere is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("\n>>> ")

        if choice == "take honey":
            dead("The bear looks at you and slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea that means.")


def cthulhu_room():
    print("\nHere you see the great Cthulu.")
    print("He, it whatever stares at you and you go insane.")
    print("Do you flee or eat your head?")

    choice = input("\n>>> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("\nYou are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do your take?")

    choice = input("\n>>> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()
