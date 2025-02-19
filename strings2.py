#         012345678901234
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3]) # w
print(parrot[4]) # e
print(parrot[9]) # ' '
print(parrot[3]) # w
print(parrot[6]) # i
print(parrot[8]) # n

print(parrot[0:6]) # Norweg
print(parrot[6:])

print(parrot[3:5])
print(parrot[0:9]) # Norwegian
print(parrot[:9]) # Norwegian - prints the same thing as providing '0' so we don't need to provide it.
print(parrot[10:]) # Blue - do not need to provide ending index if going to end of string.
print(parrot[:]) # Norwegian Blue

#          01234567890123456789012345
alphabet = 'abcdefghijklmnopqrstuvwxyz'
name = 'bartholomew'
copied_name = ''

# a very direct way of spelling out a name with the alphabet string
# print(letters[9] + letters[14] + letters[13] + letters[0] + letters[19] + letters[7] + letters[0] + letters[13])

# my very roundabout way of copying the name to another variable by using the alphabet string.
for character in name:
    copied_name += alphabet[alphabet.index(character)]

print(copied_name.capitalize())

# ======= lesson 33 - using step in a slice =========
print(parrot[0:6:2]) # Nre
print(parrot[0:6:3]) # Nw

number = '9,223;372:036 854,775;807'
separators = number[1::4]

# start at index 1 (',') and split every 4th character to the end (since no end index provided)
print(separators) # ',;: ,;'

values = "".join(char if char not in separators else " " for char in number).split()

print([int(val) for val in values])