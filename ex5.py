name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

#convert height and weight to metric
metric_height = round(height * 2.54, 1)

# the integer after the comma in round tells it where to round
# negative is to the left of decimal, positive is to the right of decimal
metric_weight = round(.4536 * weight, 1)

print()
print(f"Let's talk about {name}.")
print(f"He's {metric_height} centimeters tall.")
print(f"He weighs {metric_weight} kilograms.")
print("That sounds a lot better than pounds.")
print(f"He's got {eyes} eyes and {hair} hair, and is a flaming dooshbag.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
