# Whackamole
import time
def dream():
    print("After a weird day at work and way too much to drink,")
    time.sleep(2.5)
    print("you fall asleep and find yourself in the most vivid dream you have ever experienced.")
    time.sleep(2.5)
    print("What you see in front of you is a giant game of weird whackamole.\n")
    time.sleep(2.5)
    print("Fran Drescher is laughing at you and telling you to \'select your whacking tool.\'\n")
    time.sleep(3)
    print("\'You will receive three whacking tool choices, one at a time.\'")
    time.sleep(2.5)
    tool_pick()
def tool_pick():
    your_pick = input("""Your first whacking option is a zuccini. Do you take this whacking tool?\n
    y) yes
    n) no\n\t""")
#    your_pick = input(">>> ")

    print(f"your_pick is \'{your_pick}\'.") #debug
    if your_pick == "y" or your_pick == "yes":
        status = input("Do you take a long or short zuccini?  ")
        if "long" in status:
            status = "long"
        elif "short" in status:
            status = "short"
        else:
            status = "dipshit"
        smack("zuccini", status)
    elif your_pick == "n" or your_pick == "no":
        second_tool()
    else:
        print("Dude, wtf? Try again.\n")
        tool_pick()

def second_tool():
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
        smack("noodle", status)
    elif your_pick == "n" or your_pick == "no":
        tool = "cobra"
        cobra()
    else:
        print("Dude, wtf? Try again.\n")
        second_tool()

def smack(tool, status):
    print("You have arrived at the smack function.") #debug
    print(f"Your tool is {tool} and your status is {status}.") #debug


def cobra():
    print("You have arrived at the cobra function.") #debug
    print("You get to do your whacking with a 12 foot king cobra. Congratulations!")
    end = input("""Do you grab it from the tail or the head?
    h) head
    t) tail\n""")

    if end == "h" or end == "head":
        print("You chose to take the Cobra by the head.")
        smack("cobra", "head")
    elif end == "t" or end == "tail":
        print("You chose the Cobra tail.")
        smack("cobra", "tail")
    else:
        smack("cobra", "dipshit")

dream()
