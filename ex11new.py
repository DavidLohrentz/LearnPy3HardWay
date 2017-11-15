# line beak
print("\n")
# ask for age input
print("How old are you?", end=' ')
# put result in age
age = input()

# use alternate method to ask for input for dick length
# store result in dickinches
dickinches = int(input("How long is your dick in inches: "))
BiggerThanBannonDick = round(2.54 * dickinches, 1) - 0.5

dickft = round(dickinches / 12, 1)

# get input for ht and store in height
height = int(input("How tall are you in inches: "))

# get floor quotient of height // 12, store in alt_ft
alt_ft = height // 12

# get remainder of height % 12 and store in inches
inches = height % 12

# get wight input
print("How much do you weigh?", end=' ')
lb = input()
print("Bullshit! How many pounds do you ACTUALLY weigh?", end=' ')
# put input in lb
lb = int(input())

# get input for no. days since stopped beating wife and store in beater
beater = int(input("How many days ago did you stop beating your wife: "))
# convert days to hours
wifebeater = beater * 24 * 60

# summarize all
print(f"""\n\nSo, you're {age} years old, {alt_ft}\'{inches}\" tall, weigh {lb} lbs,
your dick is {dickft} feet long, which is {BiggerThanBannonDick} cm longer than Bannon\'s,
and you just admitted that you were beating the hell \nout of your wife until {wifebeater} minutes ago.""")
