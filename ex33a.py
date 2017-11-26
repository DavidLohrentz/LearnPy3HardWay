x = int(input("How far to iterate?\n>>> "))
y = int(input("How much to increment?\n>>> "))
numbers = []
for i in range(0, x, y):
    print(f"At the top i is {i}")
    numbers.append(i)
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

for a in numbers:
    print(a)
