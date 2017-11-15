print()
print()
# define types_of_people
types_of_people = "1,000,000"
# define x with formatted string containing variable above
x = f"There are {types_of_people} types of people."
print("<<<<<<< x after assigning value", x)
# define binary
binary = "binary"
# define do_not
do_not = "refuse to self-flaggelate"

print("<<<<<< after assigning do_not", do_not)
#define y formatted string with two variables
y = f"Those who know {binary} and those who {do_not}."

#print variable x
print(x)
# print variable y
print(y)

# print a string containing variable x
print(f"I said: {x}")
# print a string containing variable y
print(f"I also said '{y}'")

# Define variable hilarious as boolean with value of False
hilarious = False

# define T, N & G
T = True
N = "No"
G = "Eat shit and die, Trump"
# define joke_evaluation as a string with an undefined variable
joke_evaluation = "Isn't that joke so funny?! {}"

# print joke_evaluation and call hilarious to fill the empty variable
print(joke_evaluation.format(G))

#define w
w = "This is the left side of..."
# define e
e = "a banana."

print(w + e)
