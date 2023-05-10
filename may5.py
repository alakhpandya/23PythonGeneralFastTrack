s1 = "Superman came to rescue people of USA but he got confused between me, citizens and terrorists."

# difference between functions & methods:
# functions:
len(s1)
type(s1)
# methods:
s2 = s1.capitalize()    # first character capital & all other small
# print(s1)
# strings are immutable means their methods do not change the original string but, they return a new string.
"""
print(s2)
print(s1.upper())
print(s1.lower())
print(s1.swapcase())


a = "Welcome to our program!"
print(" " + "-" * 100)
# print("Welcome to our program!".center(100, "-"))
print("|" + "Welcome to our program!".center(100) + "|")
print(" " + "-" * 100)
"""
# a = s1.count("e")
# print(a)

# print(s1.count("me"))
"""
s1.index("me")
print(s1.index("e", 4))

a = s1.index("e", 4)
print(s1.index("e", a+1))

print(s1.index("e", 20, 30))
# print(s1.index("e", 19, 22))
print(s1.find("e", 19, 22))
"""
"""
print(s1.rindex("e"))
print(s1.rindex("e", 40))
print(s1.rindex("e", 0, 84))
"""
# Take a string input from user, find index number of 3rd last "e" in that string. Print -1 if 3rd last "e" does not exist in the string given by user.