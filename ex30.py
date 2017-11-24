people = 30

print(f"\nYou have {people} people.\n")

print("How many cars are there?\n>>> ")
cars = int(input())
if cars == 0:
    print("Enter a number of cars greater than 0.")
    cars = int(input())

print("How many trucks are there?\n>>> ")
trucks = int(input())
if trucks == 0:
    print("Enter a number of trucks greater than 0.")
    trucks = int(input())


if trucks / cars > 1.5:
    print("That's too many trucks.")
elif trucks < cars:
    print("Yo! Maybe we should take the trucks.")
else:
    print("We can't decide.")

ratio = people / trucks
if people / trucks < 2 and people / cars > 3:
    print(f"The people-to-truck ratio is {ratio}, so let's just take the trucks.")
elif people / cars <= 3.2 and people / cars >= 3.1:
    print("We have about Pi cars. Let's make a circle.")
else:
    print("Hey. I need pizza now!")

if cars > people:
    print("Perhaps, we should take the cars.")
elif people > (cars + trucks) and cars < people:
    print("""We have more people than vehicles, so we need both cars and trucks.""")
else:
    print("We still can't decide. I suggest unicycles.")
