from sys import argv
script, filename = argv

newfile = open(filename, 'w')
newfile.truncate()
print("\nLet's write a Minnesota Gopher haiku\n")
haiku1 = input("haiku, line 1, 5 syllables: ")
haiku2 = input("haiku, line 2, 7 syllables: ")
haiku3 = input("haiku, line 3, 5 syllables: ")

newfile.write(f"{haiku1}\n{haiku2}\n{haiku3}\n")

print(f"Here is your haiku:\n {haiku1} \n {haiku2} \n {haiku3}")

newfile.close()
