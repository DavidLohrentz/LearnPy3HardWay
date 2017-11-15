# get the argv module ready
# from sys import argv
# tell argv what to do with the command line input
#script, filename = argv
# define txt; mode r is read only
# save filename text to txt variable
# txt = open(filename, mode = 'r')
# put in a blank line at the top
print("\n")
# print a string with filename variable
# print(f"Here's your file {filename}.")
# display the text in the filename file
# print(txt.read())
# close(txt)

# now do the same thing from input here
print("Type the filename again:")
# ask for input and assign the filename to file_again variable
file_again = input("\n> ")
# open this second filename file
txt_again = open(file_again)

# display the text in this file
print(txt_again.read())
