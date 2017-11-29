# Whackamole
import time
from sys import exit
from random import randint

    # make a list of dooshbags from dooshlist.txt filed

def add_doosh(new_doosh):
    new_doosh = new_doosh + '\n'
    f = 'dooshlist.txt'
    file = open(f, 'a+')
    file.write(new_doosh)
    file.close()
    return new_doosh


def doosh_generator():
    mylist = open("dooshlist.txt").readlines()
    c = len(mylist) - 1
    print(f"number of dooshes in doooshlist is {c}.")
    a = randint(0,c)
    b = mylist[a]
    random_doosh = b.rstrip()
    print(f"random_doosh is {random_doosh}")
    initials = ''.join(name[0].lower() for name in b.split())
    # print(f"\nRandom doosh is {random_doosh} & initials are {initials}.") # debug line
    # print(f"\n{c} dooshes in doosh list.") # debug line
    return random_doosh, initials

def tool_generator():
    tool_list = ["swimming pool noodle", "zombie arm", "flower bouquet", "baguette",
    "tennis racket", "garden hose", "jellyfish", "cactus", "porcupine", "catfish",
    "cheese grater", "fettucini", "chainsaw", "cucumber", "pillow", "Pussy Willow",
    "kielbasa", "compost pile", "pencil"]
    c = len(tool_list) - 1
    global random_tool
    a = randint(0,c)
    random_tool = tool_list[a]

    global tool_initials
    tool_initials = ''.join(name[0].lower() for name in random_tool.split())

    return random_tool, tool_initials

def snake_generator():
    snake_list = ["rattlesnake", "king cobra", "black mamba", "death adder", "puff adder", "spitting cobra", "water moccasin", "Yellow Belly Sea Snake"]
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
    ["squirming", "biting"], ["creepy", "nauseating"], ["surly", "ticklish"]]
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
def dream():
    print("\nAfter a demoralizing day at work you go out on the town with your sketchiest friend.\n")
    time.sleep(2.5)
    booze = input("How many drinks did you have?  ")

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
    laugher, initials = doosh_generator()
    print("In front of you is the game of Celebrity Dooshbag Whackamole.\n")
    time.sleep(2.5)
    print(f"{laugher} is laughing at you and telling you to \'select your whacking tool.\'\n")
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
    else:
        print("Dude, wtf? Try again.\n")
        tool_pick(drunkenness)

def second_tool(drunkenness):
    print("\nYou have arrived at second_tool function.") # debug
    pause_here = input("Stopping before the problem. Hit return to continue.")
    random_tool2, tool_initial2 = tool_generator()

#    time.sleep(2)
    print(f"""The second whacking tool option is a {random_tool2}. Do you take it?\n
    y) yes
    n) no\n\t""")
    your_pick = input(">>> ")

    #print(f"your_pick is \'{your_pick}\'.") #debug
    if your_pick == "y" or your_pick == "yes":
        newstatus1, newstatus2, newinitial1, newinitial2 = status_generator()
        print(f"""\n\nChose one: \n{newstatus1} {random_tool2} ({newinitial1})
        \n{newstatus2} {random_tool2} ({newinitial2})""")
        status_answer = input("\n >>> ")

        if status_answer == newinitial1:
            status = newstatus1
        elif status_answer == newinitial2:
            status = newstatus2
        else:
            status = "dipshit"
        smack(random_tool2, status, drunkenness)
    elif your_pick == "n" or your_pick == "no":
        snake_tool(drunkenness)
    else:
        print("Dude, wtf? Try again.\n")
        second_tool(drunkenness)

def broken_zuc(whack, tool, status, drunkenness):
    print("You have arrived at broken_zuc function.")
    print(whack, tool, status, drunkenness)
    exit(0)

def smack(tool, status, drunkenness):
    print("You have arrived at the smack function.") #debug
    time.sleep(2)
    print(f"\ntool: {tool} \nstatus: {status} \ndrunkenness: {drunkenness}\n\n") #debug
    random_doosh, initials = doosh_generator()
    time.sleep(2)
    print(f"The heads of {random_doosh} and Chuck Norris pop up.\n")
    time.sleep(2)
    whack = input(f"Who do you whack?\n{random_doosh} ({initials})\nChuck Norris (cn)\n>>> ")
    print(f"You whack {whack}.")

    if drunkenness == "sloshed" and whack == initials:
        print("You fall over in a drunken stupor.")
        time.sleep(2)
        print(f"Meanwhile, {random_doosh} and Chuck Norris fight to the death.\n")
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

    elif status == "dipshit":
        print("You failed to answer correctly. Let this be a lesson to you.")
        time.sleep(2)
        print(f"{random_doosh} and Chuck Norris take away your {tool} and whack you until you have no arms or legs.\n")
        exit(0)

    elif whack == initials and tool == "zuccini" and status == "long" and drunkenness == "none":
        print(whack, tool, status, drunkenness)
        print(f"You whacked {random_doosh} so hard that your {tool} broke in half.")
        time.sleep(2)
        print(f"{random_doosh} staggers away in fear.\n")
        status = "short"
        whack = "cn"
        broken_zuc(whack, tool, status, drunkenness)

    elif whack == initials and tool == "zuccini" and status == "short" and drunkenness == "none":
        print(whack, tool, status, drunkenness)
        print(f"Congratulations! Short zuccini are {random_doosh}\'s Kryptonite.\n")
        time.sleep(2)
        print(f"{random_doosh} falls back down into the hole. Goodbye {random_doosh}.\n")
        status = "short"
        whack = "cn"
        broken_zuc(whack, tool, status, drunkenness)

    elif whack == initials and tool == "zuccini" and status == "short" and drunkenness == "buzzed":
        print(whack, tool, status, drunkenness)
        print(f"Congratulations! Short zuccini are {random_doosh}\'s Kryptonite.\n")
        time.sleep(2)
        print(f"{random_doosh} falls back down into the hole while you piss on his head.\n")
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

    else:
        print("Error")
        print(f"Have not built whack == {whack}, tool == {tool}, status == {status} & drunkenness == {drunkenness}.")
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
