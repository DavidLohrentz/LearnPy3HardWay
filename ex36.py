# Whackamole
import time
from sys import exit
from random import randint
import os
    # make a list of dooshbags from dooshlist.txt filed

global tool_list
global tool_to_check


def file_accessible(filepath, mode):
    # check if a file exists and is accessible.
    try:
        f = open(filepath, mode)
        f.close()
    except IOError as e:
        return False

def check_if_files_exist():
    dooshlist_accessible = file_accessible('dooshlist.txt', 'r')
    tool_list_accessible = file_accessible('tool_list.txt', 'r')
    if dooshlist_accessible == True and tool_list_accessible == True:
        print("The necessary list files exists in this directory.")
    elif dooshlist_accessible == False and tool_list_accessible == False:
        print("\nTo use this file, you need to create two support files.")
        time.sleep(2)
        print("You need to create a txt file named 'dooshlist.txt' and another named tool_list.txt.")
        print("Put them in this directory and load them up, one item per line.")
        exit(0)

    elif dooshlist_accessible == True and tool_list_accessible == False:
        print("To use this file you need to create a txt file named 'tool_list.txt'.")
        time.sleep(2.5)
        print("Put that file in the same directory as this file and add one whacking tool per line.")
        time.sleep(2)
        print("The more the merrier.")
        exit(0)

    elif dooshlist_accessible == False and tool_list_accessible == True:
        print("To use this file you need to create a txt file named 'dooshlist.txt'.")
        time.sleep(2.5)
        print("Put that file in the same directory as this file and add one doosh per line.")
        time.sleep(2)
        print("The more the merrier.")
        exit(0)
    else:
        print("File accessibility test failure")
        exit(0)

def add_doosh(new_doosh):
    new_doosh = new_doosh + '\n'
    f = 'dooshlist.txt'
    file = open(f, 'a+')
    file.write(new_doosh)
    file.close()
    return new_doosh

def add_tool(new_tool):
    new_tool = new_tool + '\n'
    f = 'tool_list.txt'
    file = open(f, 'a+')
    file.write(new_tool)
    file.close()
    return new_tool

def doosh_generator():
    mylist = open("dooshlist.txt").readlines()
    c = len(mylist) - 1
    print(f"number of dooshes in doooshlist is {c}.") # debug
    a = randint(0,c)
    b = mylist[a]
    random_doosh = b.rstrip()
    print(f"random_doosh is {random_doosh}") # debug
    initials = ''.join(name[0].lower() for name in b.split())
    # print(f"\nRandom doosh is {random_doosh} & initials are {initials}.") # debug line
    # print(f"\n{c} dooshes in doosh list.") # debug line
    return random_doosh, initials

def tool_generator():
    tool_list= open('tool_list.txt').readlines()
    c = len(tool_list) - 1
    global random_tool
    a = randint(0,c)
    random_tool = tool_list[a]
    random_tool = random_tool.rstrip()

    global tool_initials
    tool_initials = ''.join(name[0].lower() for name in random_tool.split())

    return random_tool, tool_initials

def snake_generator():
    snake_list = ["rattlesnake", "king cobra", "black mamba", "death adder", "puff adder", "spitting cobra",
    "water moccasin", "Yellow Belly Sea Snake", "Inland Taipan"]
    c = len(snake_list) - 1
    global random_snake
    a = randint(0,c)
    random_snake = snake_list[a]

    global snake_initials
    snake_initials = ''.join(name[0].lower() for name in random_snake.split())

    return random_snake, snake_initials

def status_generator():
    global random_status
    status_list = [["greasey", "slimey"], ["bloody", "poopy"], ["chocolate-covered", "beer-battered"], ["tiny", "gargantuan"],
    ["pink", "blue"], ["dirty", "rotten"], ["long", "short"], ["old", "kaput"], ["burning", "holey"],
    ["squirming", "biting"], ["creepy", "nauseating"], ["surly", "ticklish"], ["frisky", "lethargic"], ["epic", "dwarfish"],
    ["putrid", "fragile"], ["bloated", "emaciated"], ["leaky", "ebola-tinged"], ["Russian", "Turkish"]]
    c = len(status_list) - 1

    global random_status1
    global random_status2
    a = randint(0,c)
    random_status = status_list[a]
    random_status1 = random_status[0]
    random_status2 = random_status[1]

    global status1_initials
    global status2_initials
    status1_initials = ''.join(name[0].lower() for name in random_status1.split())
    status2_initials = ''.join(name[0].lower() for name in random_status2.split())

    return random_status1, random_status2, status1_initials, status2_initials
# ---------------------------------------------------------------
# check_if_files_exist()
def dream():
    global sketchy_friend
    sketchy_friend = input("Who is your sketchiest friend?   ")
    print(f"\nAfter a demoralizing day at work you go out on the town with {sketchy_friend}.\n")
    time.sleep(2.5)
    booze = input(f"How many drinks did you have with {sketchy_friend}?  ")
    global drunkenness
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
    print("You fall into a deep sleep and begin to dream.\n")
    time.sleep(2.5)
    print("You find yourself at an arcade game room.")
    time.sleep(2)

    # this works, but slows down testing so is commented out
    #add_doosh()
    print("In front of you is the game of Celebrity Dooshbag Whackamole.\n")
    time.sleep(2.5)
    print(f"{sketchy_friend} is laughing at you to \'select your whacking tool.\'\n")
    time.sleep(3)
    print("You will receive three whacking tool options, picking yes or no, one at a time.\n")
    #time.sleep(2.5)
    tool_pick(drunkenness)

def tool_pick(drunkenness):
    random_tool, tool_initials = tool_generator()
    your_pick = input(f"Your first whacking option is a {random_tool}. Do you take this whacking tool?\ny) yes\nn) no\t")

    # print(f"your_pick is \'{your_pick}\'.") #debug
    if your_pick == "y" or your_pick == "yes":
        random_status1, random_status2, status1_initials, status2_initials = status_generator()
        print(f"\n\nChose one: \n{random_status1} {random_tool} ({status1_initials})")
        print(f"{random_status2} {random_tool} ({status2_initials})")
        status_answer = input("\n >>> ")
        if status_answer == status1_initials:
            status = random_status1
        elif status_answer == status2_initials:
            status = random_status2
        else:
            status = "dipshit"
        smack(random_tool, status, drunkenness)
    elif your_pick == "n" or your_pick == "no":
        second_tool(drunkenness)
    elif your_pick != "n" and your_pick != "y":
        print("Dude, wtf? Try again.\n")
        tool_pick(drunkenness)
    else:
        exit(0)
def check_tool(tool_to_check):
    if tool_to_check == random_tool:
        random_tool2, tool_initial2 = tool_generator()
        return random_tool2, tool_initial2
    else:
        return random_tool2, tool_initial2

def second_tool(drunkenness):
    # print("\nYou have arrived at second_tool function.") # debug
    # pause_here = input("Stopping before the problem. Hit return to continue.")
    random_tool2, tool_initial2 = tool_generator()
    check_tool(random_tool2)
#    time.sleep(2)
    print(f"""The second whacking tool option is a {random_tool2}. Do you take it?\n
    y) yes
    n) no\n\t""")
    your_pick = input(">>> ")

    #print(f"your_pick is \'{your_pick}\'.") #debug
    if your_pick == "y" or your_pick == "yes":
        newstatus1, newstatus2, newinitial1, newinitial2 = status_generator()
        print(f"\n\nChose one: \n{newstatus1} {random_tool2} ({newinitial1})")
        print(f"{newstatus2} {random_tool2} ({newinitial2})")
        status_answer = input("\n >>> ")

        if status_answer == newinitial1:
            status = newstatus1
        elif status_answer == newinitial2:
            status = newstatus2
        elif status_answer != newinitial1 and status_answer != newinitial2:
            status = "dipshit"
        else:
            exit(0)
        smack(random_tool2, status, drunkenness)
    elif your_pick == "n" or your_pick == "no":
        snake_tool(drunkenness)
    else:
        print("Dude, wtf? Try again.\n")
        second_tool(drunkenness)

def popup2(whack, tool, status, drunkenness):
    print("You have arrived at popup2 function.") #debug
    if status == "short" or status != "melted":
        print("Put short or melted tool stuff here")
    elif status != "short" or status != "melted":
        print("Congratulations! Now that you have made it this far, you get to pick your own whacking tool.")
        b = input("Your new whacking tool:  ")
        add_tool(b)
        tool = b
    else:
        exit(0)
    print("The end.")
    exit(0)

def smack(tool, status, drunkenness):
    print("You have arrived at the smack function.") #debug
    time.sleep(2)
    print(f"\ntool: {tool} \nstatus: {status} \ndrunkenness: {drunkenness}\n\n") #debug
    global initials
    global random_doosh
    random_doosh, initials = doosh_generator()
    time.sleep(2)
    print(f"The heads of {random_doosh} and Chuck Norris pop up.\n")
    time.sleep(2)
    whack = input(f"Who do you whack?\n{random_doosh} ({initials})\nChuck Norris (cn)\n>>> ")
    # print(f"You whack {whack}.") #debug

    if status == "dipshit":
        print("You failed to answer correctly. Let this be a lesson to you.")
        time.sleep(2)
        print(f"{random_doosh} and Chuck Norris take away your {tool} and whack you until you have no arms or legs.\n")
        exit(0)
    elif drunkenness == "sloshed":
        sloshedwhack(whack, tool, status)
    elif drunkenness == "buzzed":
        buzzedwhack(whack, tool, status)
    elif drunkenness == "none":
        teetotalwhack(whack, tool, status)
    else:
        print("Drunk error")
        exit(0)

def sloshedwhack(whack, tool, status):
    if whack == initials:
        print(f"After you fall down drunk, {random_doosh} and Chuck Norris fight to the death.\n")
        time.sleep(2)
        print(f"Getting drunk and attempting to whack {random_doosh} with a {tool} was the winning answer.\n")
        time.sleep(1)
        print("Congratulations! You are the winner. Go forth and prosper.\n")
        time.sleep(1)
        doosh_prize = input("Your prize is adding a dooshbag to the list: ")
        add_doosh(doosh_prize)
        time.sleep(1)
        print(f"For a successful life, continue to drink heavily and whack random celebrity dooshbags with a {tool}.")
        exit(0)

    elif whack == "cn":
        print("Nobody takes on Chuck Norris when they are drunk.")
        print("He roundhouse kicks your head out through your ass, and now you are sort of inside out.")
        popup2('cn', tool, status, drunkenness)

    else:
        print('sloshed error')
        exit(0)

def buzzedwhack(whack, tool, status):
    if whack == initials:
        time.sleep(1.5)
        print(f"{random_doosh} has a {tool} fetish.\n")
        time.sleep(2)
        print(f"Every time you whack {random_doosh} with your {tool}, {random_doosh} says:")
        time.sleep(1.5)
        print("\'Thank you sir, may I have another\'.\n")
        time.sleep(2)
        print(f"Eventually, he takes half of your {tool} so he can sleep with it under his pillow.\n")
        time.sleep(2)
        status = "short"
        whack = random_doosh
        popup2(whack, tool, status, drunkenness)

    elif whack == "cn":
        print(f"Chuck Norris is not afraid of {tool}s.")
        time.sleep(2)
        print(f"He stares down your {tool} until it melts.\n")
        whack = "cn"
        status = "melted"
        popup2(whack, tool, status, drunkenness)

    else:
        print("teetotal error")
        exit(0)


def teetotalwhack(whack, tool, status):
    if whack == initials:
        print(f"Good thing you were sober, dealing with {random_doosh} AND Chuck Norris.")
        print(f"You whacked {random_doosh} so hard that you broke your {tool} in half.")
        time.sleep(2)
        print(f"{random_doosh} staggers away in fear.\n")
        print(f"Good luck with half of a {tool} in the next round.")
        status = "short"
        whack = "cn"
        popup2(whack, tool, status, drunkenness)

    elif whack == "cn":
        print(f"Chuck Norris has a Kryptonite and it is {status} {tool}s.")
        time.sleep(2)
        print(f"He becomes to weak to roundhouse kick and you whack him six feet under with your {tool}.\n")
        whack = random_doosh
        popup2(whack, tool, status, drunkenness)

    else:
        print("teetotal error")
        exit(0)



def snake_tool(drunkenness):
    print("You have arrived at the snake_tool function.") #debug
    time.sleep(1)
    get_snake, snake_initials = snake_generator()
    print(f"Congratulations! You get to do your whacking with a large {get_snake}.\n")
    time.sleep(2.5)
    end = input("""Do you grab it from the head or the tail?
    h) head
    t) tail\n""")

    if end == "h" or end == "head":
        if drunkenness == "sloshed":
            print(f"You are too drunk to grab a {get_snake} by the head. Take the tail instead.")
            smack(get_snake, "tail", drunkenness)
        else:
            print(f"You chose to take the {get_snake} by the head.")
            smack(get_snake, "head", drunkenness)
    elif end == "t" or end == "tail":
        print(f"You chose the {get_snake} tail.")
        smack(get_snake, "tail", drunkenness)
    else:
        smack(get_snake, "dipshit", drunkenness)

dream()
