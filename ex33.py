
def fruitloop():
    numbers = []
    i = 0
    y = int(input("How much to increment?\n>>> "))
    x = int(input("How many times to loop?\n>>> "))
    while i < x:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += y
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)
fruitloop()
