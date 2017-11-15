from sys import argv

script, user_name, dick_inches = argv
prompt = f'\n{script}\N{JAPANESE OGRE} {user_name}> '
print("\n")
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. What a fucking shit hole.
You have a {computer} and you have a {dick_inches}" dick. Nice
""")
