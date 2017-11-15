# print two blank lines
print("\n\n")

# assign DOW values to days
days = "\n\nMon Tue Wed Thu Fri Sat Sun"

# assign Jan-Aug month names to variable months
# "/n" adds a return when printing
months = "\n\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"


# print days with a string making it a sentence
print("Here are the days: ", days)

# print months with a string making it a sentence
print("\nHere are the months: ", months)

# use triple quotes to extend a string over multiple lines

line_number = 4
lineup = line_number + 1
print(f"""
\nThere's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even {line_number} lines if we want, \nor {lineup} \nor 6.
""")
