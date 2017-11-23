
x = 0
iq = 10

def eat_shit(x):
    Punk1 = 1
    X = int(input("\nHow many piles of poo? \n"))
    while Punk1 <= X / 2:
        print(f"{Punk1}\N{PILE OF POO} First Half")
        Punk1 += 1
    while Punk1 <= X * .75:
        print(f"{Punk1}\N{PILE OF POO} Half way")
        Punk1 += 1
    while Punk1 <= X:
        print(f"{Punk1}\N{PILE OF POO} Almost there")
        Punk1 += 1
    Punk1 -= 1
    print(f"\N{PILE OF POO}" * Punk1)
    print("Now SLIGHTLY more full of shit.")

def oni(x):
    X = int(input("\nHow many oni would you like to smash? \n"))
    Punk1 = 1
    while Punk1 <= X:
        print(f"\t{Punk1} \N{JAPANESE OGRE} smashing ")
        Punk1 += 1
    Punk1 -= 1
    print(f"\N{JAPANESE OGRE}" * Punk1)
    print("\n\nThoroughly smashed! Onegai Shimasu!\n")

def drop_kick():
    X = int(input("\nHow many times would you like to drop-kick? \n"))
    Punk1 = 1
    HalfX = X / 2
    while Punk1 <= X:
        if Punk1 < HalfX:
            print(f"\t{Punk1} Drop-kicking ")
            Punk1 += 1
        else:
            print(f"{Punk1} More than half way ")
            Punk1 += 1

    print("\n\Drop-kicked! Yippeee\n")

def ask():
    a = input("\nDrop kick, eat shit or smash by oni? \nType 'poop', 'oni' or 'drop_kick' (or 'dk' for short) >>> ")
    if a == "poop":
        eat_shit(x)

    elif a == "oni":
        oni(x)

    elif a == "drop_kick" or "dk":
        drop_kick()

    else:
        print("Enter a valid choice.")
        ask()

ask()
