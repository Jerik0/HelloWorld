answer = 5

print("Please guess a number between 1 and 10")
guess = int(input())

if guess == answer:
    print("Bingo! You get some booty (  Y  )")
elif guess > answer:
    print("No booty for you! Go Lower.")
elif guess < answer:
    print("No booty! Go higher.")