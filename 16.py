from sys import argv

script, filename = argv

x = open(filename, 'w')

print(x.read())

x.close()
