from sys import argv
script, trump_iq = argv
trump_iq = int(trump_iq)
counter = 0

def loop():
    global counter
    print(f"{counter} counter at line 8")
    if counter < trump_iq:
        print(f"{counter} counter at line 10")
        counter += 1
        print(f"{counter} counter at line 12")
        return loop()
loop()
