# define a new function called Cheese_and_crackers
def cheese_and_crackers (cheese_count, boxes_of_crackers, celebration, get):

# indent and print one line that uses cheese_count variable after line feed
	print(f"\nYou have {cheese_count} cheeses.")
# indent and print a line that uses boxes_of_crackers variable
	print(f"You have {boxes_of_crackers} boxes of crackers.")
# indent and print a third line using celebration variable
	print(f"Holy Fuck! That is enough for a {celebration}.")
# indent and print fourth line using get variable, insert line feed
	print(f"Go get some {get}.\n")

# print a line that says we are just going to feed it directly in code
print("We can just give the function numbers directly:")
# call function with four variables
cheese_and_crackers(20, 30, "shitstorm", "toiletpaper")

# print what we are doing this time
print("OR, we can use variables from our script:")
# Give new values to our four variables
amount_of_cheese = 10
amount_of_crackers = 50
celebration = "protest"
get = "PunkinHead Signs"

# run the function with the variables we just updated
cheese_and_crackers(amount_of_cheese, amount_of_crackers, celebration, get)

# print what we are doing now
print("We can even do math inside too:")
# show how to run the function with addtion
cheese_and_crackers(10 + 20, 5 + 6, "road trip", "camping gear")

# print what we are doing next
print("And we can even combine variables and math:")
# add to the variables we used upstream
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000, "one month", "wine")

# print what we are doing now in input prompts
# print("Or you can prompt for the variables: \n")
# prompt for the 4 values
# amount_of_cheese = input("How many cheeses do you have: \n")
# amount_of_crackers = input("How many boxes of crackers do you have: ")
# celebration = input("that is enough for a ____________ \n>>> ")
# get = input(f"go get some ____________ for your {celebration} \n>>> ")

# run the function with the input values we just received
# cheese_and_crackers(amount_of_cheese, amount_of_crackers, celebration, get)
def PunkinHead(nick, IQ, illness, days_left, prison_yrs):
	print(f"\nI call 45 {nick} because his IQ is {IQ}.")
	print(f"{nick} is afflicted with {illness}.")
	print(f"He has {days_left} days until we kick him out of the White House.")
	print(f"After that, {nick} will spend {prison_yrs} in prison.\n")
nick = "\'Asshole\'"
IQ = 20
illness = "narcissism"
days_left = 50
prison_yrs = 10
PunkinHead(nick, IQ, illness, days_left, prison_yrs)

nick = input("What do you call 45: >>> ")
IQ = input(f"What is {nick}\'s IQ: >>> ")
IQ = int(IQ)
illness = input(f"What is {nick}\'s affliction: >>> ")
days_left = input(f"How many days left until we kick {nick} out of the WH: >>> ")
days_left = int(days_left)
prison_yrs = input(f"How long will {nick} spend in the pokey: >>> ")
prison_yrs = int(prison_yrs)

PunkinHead(nick, IQ / 2, illness, days_left, prison_yrs)

PunkinHead("Stupid", IQ, "obtuseness", days_left, "the rest of his life")

PunkinHead(illness, prison_yrs, illness, prison_yrs, prison_yrs)

prison_yrs = input("How long will 45 spend in prison after his current gig: >>> ")
days_left = input("How many days until 45 is booted out >>> ")
days_left = int(days_left)
IQ = 50
nick = input("What do you call 45: >>> ")
illness = "brainlessness"

PunkinHead(nick, IQ, illness, days_left + 50, prison_yrs)
