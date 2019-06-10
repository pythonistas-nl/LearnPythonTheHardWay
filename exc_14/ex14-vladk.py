from sys import argv
script, user_name, camelName = argv
big = '#'
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(big)

print(f"Where do you live {user_name}?")
lives = input(big)

print("What kind of computer do you have?")
computer = input(big)
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.  Not sure where that is.
And you have a {computer} computer.  Nice.
Your {camelName} is Camel. 
""")