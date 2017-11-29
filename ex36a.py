import time
from sys import exit
from random import randint
# make a long list of dooshbags from dooshlist.txt file

mylist = open("dooshlist.txt").readlines()
c = len(mylist)
a = randint(0,c)
b = mylist[a]
initials = ''.join(name[0].lower() for name in b.split())
print(b)
print(initials)

# first pop up
tool = input("\ntool: ")
status = input("status: ")
drunkenness = input("drunkenness: ")

def broken_zuc(whack, tool, status, drunkenness):
    print("You have arrived at broken_zuc function.")
    print(whack, tool, status, drunkenness)
    exit(0)

print(f"The heads of {b} and Chuck Norris pop up.\n")
time.sleep(2)
whack = input(f"Who do you whack?\n{b} ({initials})\nChuck Norris (cn)\n>>> ")
print(f"You whack {whack}.")
if whack == (b or initials) and tool == "zuccini" and status == "long" and drunkenness == "none":
    print(whack, tool, status, drunkenness)
    print(f"You whack {b} so hard that your zuccini breaks.")
    time.sleep(2)
    print(f"{b} staggers away in fear.\n")
    status = "short"
    whack = "cn"
    broken_zuc(whack, tool, status, drunkenness)

elif whack == "cn" and tool == "zuccini" and status == "long" and drunkenness == "none":
    print(whack, tool, status, drunkenness)
    print("Before you can whack him, Chuck Norris breaks your zuccini in half with a roundhouse kick.")
    time.sleep(2)
    print(f"You fail to eliminate Cuck Norris. However he gets rid of {b} with a roundhouse kick.\n")
    status = "short"
    broken_zuc(whack, tool, status, drunkenness)

elif whack == "cn" and tool == "zuccini" and status == "long" and drunkenness == "sloshed":
    print(whack, tool, status, drunkenness)
    print("You are so drunk that you fall down before Norris hits you with a roundhouse kick.")
    time.sleep(2)
    print(f"The wind vortex from his kick blows away {b} and breaks your zuccini in half.\n")
    status = "short"
    broken_zuc(whack, tool, status, drunkenness)

else:
    print("Error")
    exit(0)
