# Whackamole
import time
from sys import exit
from random import choice, randint
import os
    # make a list of dooshbags from dooshlist.txt filed

global tool_list
global tool_to_check
global word_list
global friend_types
global friend_type

word_list = ["a demoralizing", "an exciting", "a sordid", "a discouraging", "an upsetting", "a soul-crushing", "a depressing", "a thrilling", "a dangerous", "job-killing", "a sensational", "a rip-roaring", "an electrifying", "a titilating", "an arousing"]
friend_types = ["sketchiest", "most excitable", "jumpiest", "ugliest", "most conspiratorial", "most doinkable", "most flamboyant", "weirdest", "most bizarre", "most desperate"]

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
    moods_accessible = file_accessible('moods.txt', 'r')

    if dooshlist_accessible == False:
        print("You need to create a txt file named \'dooshlist.txt\' in this directory.")
        exit(0)

    else:
        print("\'dooshlist.txt\' exists in this directory.")

    if tool_list_accessible == False:
        print("You need to create a txt file named \'tool_list.txt\' in this directory.")
        exit(0)

    else:
        print("\'dooshlist.txt\' exists in this directory.")

    if moods_accessible == False:
        print("You need to create a txt file named \'moods.txt\' in this directory.")
        exit(0)

    else:
        print("\'moods.txt\' exists in this directory.\n")

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

def word_generator():
    random_word = choice(word_list)
    return random_word

def friend_type_generator():
    friend_type = choice(friend_types)
    return friend_type

def doosh_generator():
    mylist = open("dooshlist.txt").readlines()
    b = choice(mylist)
    random_doosh = b.rstrip()
    initials = initial_maker(random_doosh)

    return random_doosh, initials

def mood_generator():
    a = open('moods.txt').readlines()
    random_mood = choice(a)
    random_mood = random_mood.rstrip()
    mood_initials = initial_maker(random_mood)

    return random_mood, mood_initials

def initial_maker(name_to_be_initialled):
    myinitials = ''.join(name[0].lower() for name in name_to_be_initialled.split())
    return myinitials

def tool_generator():
    tool_list= open('tool_list.txt').readlines()
    global random_tool
    random_tool = choice(tool_list)
    random_tool = random_tool.rstrip()
    tool_initials = initial_maker(random_tool)

    return random_tool, tool_initials

def snake_generator():
    snake_list = ["rattlesnake", "king cobra", "black mamba", "death adder", "puff adder", "spitting cobra",
    "water moccasin", "Yellow Belly Sea Snake", "Inland Taipan", "Anaconda", "Tiger Snake"]
    global random_snake
    random_snake = choice(snake_list)
    snake_initials = initial_maker(random_snake)

    return random_snake, snake_initials

def status_generator():
    global random_status
    global random_status1
    global random_status2

    status_list = [["greasey", "slimey"], ["bloody", "poopy"], ["chocolate-covered", "beer-battered"], ["tiny", "gargantuan"], ["pink", "blue"], ["dirty", "rotten"], ["long", "short"], ["old", "kaput"], ["burning", "holey"], ["squirming", "biting"], ["creepy", "nauseating"], ["surly", "ticklish"], ["frisky", "lethargic"], ["raw", "cooked"], ["flat", "roundish"], ["epic", "dwarfish"], ["soft", "fragile"], ["bloated", "emaciated"], ["leaky", "ebola-tinged"], ["Russian", "Turkish"], ["operatic", "shrill"], ["wide", "narrow"]]
    random_status = choice(status_list)
    random_status1 = random_status[0]
    random_status2 = random_status[1]
    status1_initials = initial_maker(random_status1)
    status2_initials = initial_maker(random_status2)

    return random_status1, random_status2, status1_initials, status2_initials
# ---------------------------------------------------------------

def dream():
    random_word = word_generator()
    friend_type = friend_type_generator()
    global friend_name
    friend_name = input(f"Who is your {friend_type} friend?   ")
    joke = rand_joke()
    print(joke)
    print(f"\nAfter a {random_word} day at work you go out on the town with {friend_name}.\n")
    time.sleep(2.5)
    drinks()

def drinks():
    booze = input(f"How many drinks did you have with {friend_name}?  ")
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
        drinks()
    elif int(cooked) < 0:
        print("\nYo! Enter a number greater than zero.")
        drinks()
    elif int(cooked) == 0:
        drunkenness = "none"
    elif int(cooked) < 5:
        drunkenness = "buzzed"
    elif int(cooked) >= 5:
        drunkenness = "sloshed"
    else:
        print("Code problem calculating drunk conditional")
        exit(0)
    print(f"After you have {cooked} drinks with {friend_name}, you fall into a deep sleep and begin to dream.\n")
    time.sleep(2.5)
    arcade_descriptor = word_generator()
    print(f"You find yourself at {arcade_descriptor} old school arcade room.\n")
    time.sleep(2)

    print("In front of you is the game of Celebrity Dooshbag Whackamole.\n")
    time.sleep(2.5)

    print(f"{friend_name} is laughing at you to \'select your whacking tool.\'\n")
    time.sleep(3)
    print("You will receive three whacking tool options, picking yes or no, one at a time.\n")
    #time.sleep(2.5)
    tool_pick(drunkenness)

def tool_pick(drunkenness):
    random_tool, tool_initials = tool_generator()
    your_pick = input(f"Your first whacking option is a {random_tool}. Do you take this whacking tool?\ny) yes\nn) no\n>>> ")

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

def rand_joke():
    a = randint(0, 20)
    if a == 0:
        return "We checked your references and it seems you have no friends. We'll pretend you do have one."
    else:
        return ""

def second_tool(drunkenness):
    # print("\nYou have arrived at second_tool function.") # debug
    # pause_here = input("Stopping before the problem. Hit return to continue.")
    random_tool2, tool_initial2 = tool_generator()
    check_tool(random_tool2)
#    time.sleep(2)

    your_pick = input(f"\nYour second whacking tool option is a {random_tool2}. Do you take this whacking tool?\ny) yes\nn) no\n>>> ")

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


def smack(tool, status, drunkenness):
    global initials
    global random_doosh
    random_doosh, initials = doosh_generator()
    time.sleep(2)
    random_doosh_mood, a = mood_generator()
    print(f"\nThe heads of {random_doosh} and Chuck Norris pop up from the Whackamole table.\n")
    time.sleep(2)
    print(f"There is something odd about {random_doosh}, who seems unusually {random_doosh_mood}.")
    time.sleep(2)
    whack = input(f"Who do you whack with your {tool}?\n{random_doosh_mood} {random_doosh} ({initials})\nChuck Norris (cn)\n>>> ")
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
        print(f"Getting drunk and attempting to whack {random_doosh} with a {status} {tool} was the winning answer.\n")
        time.sleep(1)
        print("Congratulations! You are the winner. Go forth and prosper.\n")
        time.sleep(1)
        doosh_prize = input("Your prize is adding a dooshbag to the list: ")
        add_doosh(doosh_prize)
        time.sleep(1)
        print(f"For a successful life, continue to drink heavily and whack random celebrity dooshbags with a {status} {tool}.\n")
        exit(0)

    elif whack == "cn":
        print("Nobody takes on Chuck Norris when they are drunk.\n")
        time.sleep(2)
        print("He roundhouse kicks your head out through your ass, and now you are permanently inside out.\n")
        time.sleep(2)
        print("However, Chuck Norris has mercy on you and let's you pick a new whacking tool, whatever you want.\n")
        time.sleep(2)
        b = input("Your new whacking tool:  ")
        add_tool(b)
        tool = b
        popup2('Chuck Norris', tool, status, drunkenness)

    else:
        print('sloshed error')
        exit(0)

def buzzedwhack(whack, tool, status):
    if whack == initials:
        time.sleep(1.5)
        print(f"Lucky for you, {random_doosh} has a {tool} fetish.\n")
        time.sleep(2)
        print(f"Every time you whack {random_doosh} with your {status} {tool}, {random_doosh} screams:")
        time.sleep(1.5)
        print("Thank you sir, may I have another?")
        time.sleep(2)
        print(f"{random_doosh} bites your {tool} in half and takes it home to sleep with at night.\n")
        time.sleep(2)

        print("However, Chuck Norris has mercy on you and let's you pick a new whacking tool, whatever you want.\n")
        time.sleep(2)
        b = input("Your new whacking tool:  ")
        add_tool(b)
        tool = b
        popup2(random_doosh, tool, status, drunkenness)

    elif whack == "cn":
        print(f"Chuck Norris is not afraid of {status} {tool}s.")
        time.sleep(2)
        print(f"He stares down your {tool} until it melts.\n")
        status = "melted"
        popup2("Chuck Norris", tool, status, drunkenness)

    else:
        print("teetotal error")
        exit(0)


def teetotalwhack(whack, tool, status):
    if whack == initials:
        print(f"Good thing you were sober, dealing with {random_doosh} AND Chuck Norris.\n")
        time.sleep(2)
        print(f"You whacked {random_doosh} so hard that you broke your {status} {tool} in half.")
        time.sleep(2)
        print(f"{random_doosh} staggers away, never to be seen again.\n")
        time.sleep(1)
        print(f"Good luck with half of a {tool} in the next round.\n")
        time.sleep(2)
        status = "short"
        whack = "Chuck Norris"
        popup2(whack, tool, status, drunkenness)

    elif whack == "cn":
        print(f"Chuck Norris has a Kryptonite and it is {status} {tool}s.")
        time.sleep(2)
        print(f"He becomes too weak to roundhouse kick and you whack him six feet under with your {tool}.\n")
        whack = random_doosh
        popup2(whack, tool, status, drunkenness)

    else:
        print("teetotal error")
        exit(0)



def snake_tool(drunkenness):
    # print("You have arrived at the snake_tool function.") #debug
    time.sleep(1)
    get_snake, snake_initials = snake_generator()
    print(f"\nCongratulations!")
    time.sleep(2)
    print(f"You have won the opportunity to do your whacking with a deadly {get_snake}.\n")
    time.sleep(2.5)
    snake_type = input(f"Pick one:\nh) hungry {get_snake}\na) angry {get_snake}\n>>> ")

    if snake_type == "h" or snake_type == "hungry":
        smack(get_snake, "hungry", drunkenness)
    elif snake_type == "a" or snake_type == "angry":
        smack(get_snake, "angry", drunkenness)
    else:
        smack(get_snake, "dipshit", drunkenness)

def popup2(whack, tool, status, drunkenness):
    print("You have arrived at popup2 function.\n") #debug
    print(f"Arrival values: whack: {whack}, tool: {tool}, status: {status}, drunkenness {drunkenness}\n")
    level2_doosh, ldi = doosh_generator()
    time.sleep(2)
    print(f"{level2_doosh} pops up through a new hole, along with {whack} who is still there.\n")
    time.sleep(3)
    if status == "short" or status != "melted":
        print(f"You try to whack, but your {tool} is totally worthless for whacking.\n")
        time.sleep(2)
        print(f"{level2_doosh} and {whack} chew off your fingers, and you will never whack again.")
        exit(0)
    elif whack == "Chuck Norris":
        print(f"Chuck Norris is mad. He roundhouse kicks you, {level2_doosh}, your {status} {tool},\n")
        print("the Whackamole table, the arcade, and the rest of the city.")
        time.sleep(3)
        print("Let's just say you will not wake up feeling refreshed.")
        exit(0)
    elif whack == {level2_doosh}:
        print(f"{level2_doosh} convinces you to take up Gandhian nonviolence rather than whacking your way through life with a {status} {tool}.")
        print(f"You put down your {status} {tool}, and never pick up another one as long as you live.")
        exit(0)
    elif status != "short" or status != "melted":
        print("Something something")
        exit(0)

    else:
        exit(0)
    print("The end.")
    exit(0)

check_if_files_exist()
dream()
