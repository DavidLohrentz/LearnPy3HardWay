from sys import argv

script, input_file = argv

def print_all(g):
    print(g.read())

def rewind(g):
    g.seek(0)

def print_a_line(line_count, g):
    print(line_count, g.readline())

current_file = open(input_file)

print("First, let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
