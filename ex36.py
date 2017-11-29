# Whackamole
import time
from sys import exit

def dream():
    print("After a weird day at work and way too much to drink,")
    time.sleep(2.5)
    print("you fall asleep and find yourself in the most vivid dream you have ever experienced.\n")
    time.sleep(2.5)
    booze = input("How many bottles of beer did you drink?  ")

    goldnum = []
    a = ""
    for i in list(booze):
        if i.isdigit():
            goldnum.append(i)
    cooked = a.join(goldnum)
    n = len(cooked)
    if n == 0:
        print("\nInclude a number in your answer, dumbass.")
        dream()
    elif int(cooked) == 0:
        drunkenness = "none"
    elif int(cooked) < 5:
        drunkenness = "buzzed"
    else:
        drunkenness = "sloshed"
    print("What you see in front of you is a giant game of weird whackamole.\n")
    time.sleep(2.5)
    print("Fran Drescher is laughing at you and telling you to \'select your whacking tool.\'\n")
    time.sleep(3)
    print("You will receive three whacking tool choices, one at a time.\n")
    time.sleep(2.5)
    tool_pick(drunkenness)

def tool_pick(drunkenness):
    your_pick = input("Your first whacking option is a zuccini. Do you take this whacking tool?\ny) yes\nn) no\t")

    print(f"your_pick is \'{your_pick}\'.") #debug
    if your_pick == "y" or your_pick == "yes":
        status = input("Do you take a long or short zuccini?  ")
        if "long" in status:
            status = "long"
        elif "short" in status:
            status = "short"
        else:
            status = "dipshit"
        smack("zuccini", status, drunkenness)
    elif your_pick == "n" or your_pick == "no":
        second_tool(drunkenness)
    else:
        print("Dude, wtf? Try again.\n")
        tool_pick(drunkenness)

def second_tool(drunkenness):
    print("You have arrived at second_tool function.") # debug
    print("""Your second option is a swimming pool noodle. Do you select this whacking tool?\n
    y) yes
    n) no\n\t""")
    your_pick = input(">>> ")

    print(f"your_pick is \'{your_pick}\'.") #debug
    if your_pick == "y" or your_pick == "yes":
        status = input("pink or blue?  ")
        if "pink" in status:
            status = "pink"
        elif "blue" in status:
            status = "blue"
        else:
            status = "dipshit"
        smack("noodle", status, drunkenness)
    elif your_pick == "n" or your_pick == "no":
        tool = "cobra"
        cobra(drunkenness)
    else:
        print("Dude, wtf? Try again.\n")
        second_tool(drunkenness)

def smack(tool, status, drunkenness):
    print("You have arrived at the smack function.") #debug
    print(f"\ntool: {tool} \nstatus: {status} \ndrunkenness: {drunkenness}\n\n") #debug
    first_whack = input(f"Straight away, Tom Crean and Roy Moore pop up. Which one do you whack with your {tool}? >>> ")
    print(f"Your first whack is {first_whack}")
    exit(0)


def cobra(drunkenness):
    print("You have arrived at the cobra function.") #debug
    print("Congratulations! You get to do your whacking with a 12 foot king cobra.\n")
    time.sleep(2.5)
    end = input("""Do you grab it from the tail or the head?
    h) head
    t) tail\n""")

    if end == "h" or end == "head":
        print("You chose to take the Cobra by the head.")
        smack("cobra", "head", drunkenness)
    elif end == "t" or end == "tail":
        print("You chose the Cobra tail.")
        smack("cobra", "tail", drunkenness)
    else:
        smack("cobra", "dipshit", drunkenness)

dream()
