moron_iq = 80
trump_iq = 0


def test_if(trump_iq, moron_iq):
    trump_iq = int(input("\nwhat is PunkinHead's IQ?\n>>>  "))
    if trump_iq <= moron_iq:
        return "What a moron."

    else:
        return "Only stupid people think he is that smart."


a = test_if(trump_iq, moron_iq)

print(a)
