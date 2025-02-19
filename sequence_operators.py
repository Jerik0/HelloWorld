# ======= lesson 36 - sequence operators =========
string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"
print(string1 + string2 + string3 + string4 + string5)

print("hello" * 5) # hellohellohellohellohello (so weird)

# print("hello" * 5 + 4) # error because concatenation and math operations can't work like this.
print("hello" *  (5 + 4))
print("hello" *  5 + "4")

today = "friday"
print("day" in today) # True
print("fri" in today) # True
print("thur" in today) # False
print("parrot" in 'fjord') # False
