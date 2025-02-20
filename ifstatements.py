name = input("Please enter your name: ")
age = int(input(f"How old are you, {name}? "))

if age > 18:
    print(f"Welcome to the voter's club, {name}!")
else:
    print(f"Sorry, {name}, please come back in {18 - age} years.")
