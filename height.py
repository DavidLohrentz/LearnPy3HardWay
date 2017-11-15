print("\n")
ht = int(input("How tall are you in inches: "))
print("<<<<<<<<<< after assigning ht", ht)
ft = ht // 12
in = int(ht % 12)
print(f"You are {ft}\'{in}\".")
