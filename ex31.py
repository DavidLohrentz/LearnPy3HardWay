print("""You enter an old bakery with two unmarked doors.
Do you go through the purple door or or the black door?""")
print("1. purple")
print("2. black")

door = input(">>> ")

if door == "1":
    print("There's a cake and a cast iron frying pan.")
    print("What do you do?\n")
    print("1. Take the cake.")
    print("2. Take the frying pan.\n")
    cakepan = input(">>> ")
    if cakepan == "1":
        print("\nDid you leave it in the rain?\n>>> ")
        print("1. Yes")
        print("2. No.")
        rain = input("\n>>> ")
    elif cakepan == "2":
        print("\nWhat did you fry?\n>>> ")
        print("1. Bacon.")
        print("2. Nothing; save it for self-defense.")
        bacon = input("\n>>> ")
        if bacon == "1":
            print("Eat it or put in your pocket?")
            print("1. Eat it.")
            print("2. Put in pocket.\n")
            bacon_pocket = input(">>> ")

    if cakepan == "1":
        if rain == "1":
            print("You can't take it because it took too long to bake it. Oh no!")
        elif  rain == "2":
            print("You'll never have the recipe again. Oh No!")
        else:
            print("You are pressed like a striped pair of pants. Good job!")
    elif cakepan == "2":
        if bacon == "1":
            if bacon_pocket == "1":
                print("You are free to go if you can make up a song about bacon.")
            else:
                print("Why on earth would you do anything but eat bacon straight away?")
                print("You have failed your bacon challenge.")
        elif bacon == "2":
            print("You accidentally drop it on your toe and it turns green.")
            print("You could have had bacon. Next time opt for bacon.")
        else:
            print("You are going to wish you had some bacon. Good job!")
    else:
        print("Well, that was a lot dumber than options 1 or 2.")
        print("You get to spend Christmas listening to elevator music.")

elif door == "2":
    print("Santa Claus is standing there with a meat cleaver.")
    print("1. Stop, drop and roll.")
    print("2. Give him a wish list.")
    print("3. Sit on his lap.\n")

    insanity = input(">>> ")

    if insanity == "1":
        print("Just because he is wearing red doesn't mean it is a fire.")
        print("Santa chops off your pinky. Good job.")
    elif insanity == "2":
        print("Santa chops your list in half and wipes his ass with them.")
        print("What did you expect from a cleaver-wielding Santa?")
    elif insanity == "3":
        print("Is that a flashlight in his pocket?")
        print("Good job!")
    else:
        print("Run for your life. This is not good Santa.")
        print("Good job!")
else:
    print("What makes you think you can outsmart the game?")
    print("An Aka Oni chases you around the block. Good job!")
