def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} + {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("\nLet's do some math with just functions:\n")

age = add(30, 27)
height = subtract(190,2)
weight = multiply(70, 4)
iq = int(divide(300, 2))

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# a puzzle for extra credit; type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print(what)
