formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter.format("\n Trump", "sucks", "ding", "dongs"),
formatter.format("because", "he", "has", "no brain.\n"),
formatter.format("What", "does", "that", "say"),
formatter.format("about", "the retards", "who voted", "for him?\n")))
print(formatter.format(
    "\tKnock knock\n",
    "\tWho's there? \n",
    "\tDonald Trump \n",
    "\tEat shit and die, asshole!\n\n"
))
print(formatter.format(formatter.format(1, 2, 3, 4), 5, 6, 7))
