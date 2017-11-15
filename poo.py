
x = 0
iq = 10

def eat_shit_punkinhead(x):
    Punk1 = 1
    X = int(input("\nHow many piles of poo would you like PunkinHead to eat? \n"))
    while Punk1 <= X / 2:
        print(f"{Punk1}\N{PILE OF POO}\N{JACK-O-LANTERN} [{Punk1} / {x }]")
        Punk1 += 1
    while Punk1 <= X * .75:
        print(f"{Punk1}\N{PILE OF POO}\N{JACK-O-LANTERN} Half way")
        Punk1 += 1
    while Punk1 <= X:
        print(f"{Punk1}\N{PILE OF POO}\N{JACK-O-LANTERN} Almost there")
        Punk1 += 1
    Punk1 -= 1
    print(f"\N{PILE OF POO}" * Punk1)
    print("\n\nPunkinHead is now SLIGHTLY more full of shit than he was.\n")

def oni(x):
    X = int(input("\nHow many oni would you like to smash PunkinHead? \n"))
    Punk1 = 1
    while Punk1 <= X:
        print(f"\t{Punk1} \N{JAPANESE OGRE} smashing \N{JACK-O-LANTERN}")
        Punk1 += 1
    Punk1 -= 1
    print(f"\N{JAPANESE OGRE}" * Punk1)
    print("\n\nPunkinHead thoroughly smashed! Happy Halloween!\n")

def torture():
    X = int(input("\nHow many times would you like to torture PunkinHead? \n"))
    Punk1 = 1
    HalfX = X / 2
    while Punk1 <= X:
        if Punk1 < HalfX:
            print(f"\t{Punk1} torturing \N{JACK-O-LANTERN}")
            Punk1 += 1
        else:
            print(f"{Punk1} More than half way \N{JACK-O-LANTERN}")
            Punk1 += 1

    print("\n\nPunkinHead thoroughly tortured! Yippeee\n")

def ask():
    a = input("\nTorture PunkinHead or watch him eat shit or be smashed by oni? \nType 'poop', 'oni' or 'torture' >>> ")
    if a == "poop":
        eat_shit_punkinhead(x)

    elif a == "oni":
        oni(x)

    elif a == "torture":
        torture()

    else:
        ask()

ask()
