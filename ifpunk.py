# python3.6 ifpunk.py
import sys

a = 50
b = 100
idiot = "What a fuckin' idiot."
sad = "Unpresidented. Sad!"
wrong = "WRONG!!!!"
IQ = 0
print(f">>>> wrong: {wrong}")

def ask_iq():
    IQ = input("What is PunkinHead's IQ:  ")
    print(f">>>> IQ: {IQ}")

def all_done():
    print("all done")

def P_IQ():
    print(">>>>>> P_IQ")
    if IQ < a:
        print(idiot)
        all_done()

    elif IQ < b:
        print(sad)
        all_done()

    else:
        print(wrong)
        ask_iq()


ask_iq()
P_IQ()
all_done()
