# ======= lesson 34 - using negative step =========
letters = 'abcdefghijklmnopqrstuvwxyz'
backwards = letters[25:0:-1]
backwards2 = letters[::-1]
print(backwards)
print(backwards2)

challenge1 = letters[-10:-13:-1]
print(challenge1) # qpo

challenge2 = letters[4::-1]
print(challenge2) # edcba

challenge3 = letters[:-9:-1]
print(challenge3) # zyxwvuts

# ======= lesson 35 - slicing idioms =========
print(letters[-4:]) # used for getting the last n values from a list.
print(letters[-1:])

print(letters[:1]) # this is the same thing as letters[0] but doesn't produce an error, produces empty string.
print(letters[0]) # this will produce an error if the string is empty.