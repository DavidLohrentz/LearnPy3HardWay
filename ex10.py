
# assign tab and string to tabby_cat
cf = "Cat Food"
x = "Fishies"
y = "\t* Catnip\n\t* Grass\n\t* Litter\n\t* kibble"
z = "\t* NothingBurger\n\t* Hairball\n\t* cat bell\n\t* Christmas cat photo"

tabby_cat = "\tI'm tabbed in."

# assign return in the middle of string and call it
# persian_cat
persian_cat = "I'm split\non a line"

# assign string and backslashes to backslash_Cat
backslash_cat = "I'm \\ a \\ cat"

# assign list values to a multi-line string
fat_cat = f'''
I'll do a list:
\n\t* {cf}
\t* {x}
{y}
{z}
'''
# print the 4 variables in this file
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
