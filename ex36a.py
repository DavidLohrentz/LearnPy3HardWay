import time
from sys import exit
from random import randint
# make a long list of dooshbags
# pull one random name from the list to dispatch with so game has a lot of variation
mylist = ["Tom Cruise", "Jean-Claude Van Damm", "Steven Seagal", "David Hasselhoff",
"Sarah Palin", "Ted Cruz", "Michele Bachmann", "Newt Gingrich", "Geraldo Rivera", "Tucker Carlson",
"Tom Crean", "P.J. Fleck"]
c = len(mylist)
a = randint(0,c)
b = mylist[a]
print(f"\nRandom dooshbag: {b}")
# first pop up
tool = input("\ntool: ")
status = input("status: ")
drunkenness = input("drunkenness: ")

def broken_zuc(whack, tool, status, drunkenness):
    print("You have arrived at broken_zuc function.")
    print(whack, tool, status, drunkenness)
    exit(0)

print("The heads of Tom Crean and Chuck Norris pop up.\n")
time.sleep(2)
whack = input(f"Who do you whack tc)\ncn)\n>>> ")
print(f"You whack {whack}.")
if whack == "tc" and tool == "zuccini" and status == "long" and drunkenness == "none":
    print(whack, tool, status, drunkenness)
    print("You whack Crean so hard that your zuccini breaks.")
    time.sleep(2)
    print("Crean runs away sucking his thumb.\n")
    status = "short"
    whack = "cn"
    broken_zuc(whack, tool, status, drunkenness)

elif whack == "cn" and tool == "zuccini" and status == "long" and drunkenness == "none":
    print(whack, tool, status, drunkenness)
    print("Before you can whack him, Chuck Norris breaks your zuccini in half with a roundhouse kick.")
    time.sleep(2)
    print("You fail to eliminate Cuck Norris. However he gets rid of Crean with a roundhouse kick.\n")
    status = "short"
    broken_zuc(whack, tool, status, drunkenness)

elif whack == "cn" and tool == "zuccini" and status == "long" and drunkenness == "sloshed":
    print(whack, tool, status, drunkenness)
    print("You are so drunk that you fall down before Norris hits you with a roundhouse kick.")
    time.sleep(2)
    print("The wind vortex from his kick blows away Crean and breaks your zuccini in half.\n")
    status = "short"
    broken_zuc(whack, tool, status, drunkenness)

else:
    print("Error")
    exit(0)
