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