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
        print(f"{cooked} is the winning number this time. Congratulations.")
        exit(0)
    else:
        under_cooked = int(cooked) - 1
        dead(f"Too bad. {under_cooked} was the winning number this time.")
        print("Tom Crean will now come up through the trap door and talk at you until you die of boredom.")

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
    print(why, "You have been a great contestant, but now you must deal with Clappy the Clown.")
    exit(0)

def start():
    print("\nYou are in a dark room.")
    print("There are doors to your right and left, and a trap door below.")
    print("Which one do your take?")

    choice = input("\n>>> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif "trap" in choice:
        basement()
    else:
        dead("You stumble around the room until you starve.")

def basement():
    print("\nTom Crean is there in a clown suit doing card tricks. He asks you to pick a card.")
    print("What card do you pick?")

    choice = (input(">>> "))

    if "king" in choice.lower() or "ace" in choice.lower() or "queen" in choice.lower() or "jack" in choice.lower():
        print("You picked a face card. Kick Tom Crean in the balls and you win.")
        exit(0)
    else:
        print("You didn't pick a face card so you lose.")
        print("However, if you fart on Clappy the Clown, you can escape.")
        exit(0)


start()
