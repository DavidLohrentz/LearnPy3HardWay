from sys import argv

script, filename = argv

display_txt = open(filename)

print(display_txt.read())

x = input("\nType the filname again \N{JAPANESE OGRE}>> ")
y = open(x)

print(y.read())
