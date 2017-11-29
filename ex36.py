# Whackamole
import time
from sys import exit
from random import randint
# make a list of dooshbags from dooshlist.txt file
mylist = open("dooshlist.txt").readlines()
c = len(mylist)
a = randint(0,c)
b = mylist[a]
random_doosh = b.rstrip()
initials = ''.join(name[0].lower() for name in b.split())
print(f"\nRandom doosh is {random_doosh} & initials are {initials}.") # debug line
print(f"\n{c} dooshes in doosh list.") # debug line

def dream():
    print("After a VERY weird day at work and you got out for drink.\n")
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
    print("you fall asleep and begin to dream.\n")
    time.sleep(2.5)
    print("You find yourself at an arcade game room.")
    time.sleep(2)
    print("The price of admission is to enter the name of a dooshbag.")
    new_doosh = input(">>> ")
    new_doosh = new_doosh + '\n'
    f = 'dooshlist.txt'
    file = open(f, 'a+')
    file.write(new_doosh)
    file.close()

    print("In front of you is a giant game of weird whackamole.\n")
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

def broken_zuc(whack, tool, status, drunkenness):
    print("You have arrived at broken_zuc function.")
    print(whack, tool, status, drunkenness)
    exit(0)

def smack(tool, status, drunkenness):
    print("You have arrived at the smack function.") #debug
    print(f"\ntool: {tool} \nstatus: {status} \ndrunkenness: {drunkenness}\n\n") #debug

    print(f"The heads of {random_doosh} and Chuck Norris pop up.\n")
    time.sleep(2)
    whack = input(f"Who do you whack?\n{random_doosh} ({initials})\nChuck Norris (cn)\n>>> ")
    print(f"You whack {whack}.")
    if whack == (random_doosh or initials) and tool == "zuccini" and status == "long" and drunkenness == "none":
        print(whack, tool, status, drunkenness)
        print(f"You whacked {random_doosh} so hard that your zuccini broke.")
        time.sleep(2)
        print(f"{random_doosh} staggers away in fear.\n")
        status = "short"
        whack = "cn"
        broken_zuc(whack, tool, status, drunkenness)

    elif whack == "cn" and tool == "zuccini" and status == "long" and drunkenness == "none":
        print(whack, tool, status, drunkenness)
        print("Before you can whack him, Chuck Norris breaks your zuccini in half with a roundhouse kick.")
        time.sleep(2)
        print(f"You failed to eliminate Cuck Norris. However he gets rid of {random_doosh} with a roundhouse kick.\n")
        status = "short"
        broken_zuc(whack, tool, status, drunkenness)

    elif whack == "cn" and tool == "zuccini" and status == "long" and drunkenness == "sloshed":
        print(whack, tool, status, drunkenness)
        print("You are so drunk that you fell down before Norris hit you with his roundhouse kick.")
        time.sleep(2)
        print(f"The wind vortex from his kick blew away {random_doosh} and broke your zuccini in half.\n")
        status = "short"
        broken_zuc(whack, tool, status, drunkenness)

    else:
        print("Error")
        exit(0)

# ---------------------------------------------------------------
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
