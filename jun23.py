# How to create empty set, methods of set, dictionaries, functions
# s = {"Kit kat", "5 star", "Dairy Milk", "Munch", "Perk", "Milky Bar", "Fuse"}

# s.add("Dairy Milk Silk")
# print(s)
# s.add("Perk")
# s.append("Perk")
# print(s)
# s1 = {1, 13, 24, 56, 13, 44, 66, 78, 87, 31, 13, 20}
# print(len(s1))
# print(s1)

# s2 = s1.clear()
# print(s2)
# print(s1)
# print(type(s1))
# print(len(s1))

# del s1
"""
s2 = s1.copy()
s3 = s1

s1.add(1000)

print("s1 =", s1)
print("s2 =", s2)
print("s3 =", s3)
"""

# s1.discard(44)
# s1.discard(13)
# print(s1)

"""
A class has 50 students. 30 students of that class got more than 60 marks in Maths. 40 students of that class got more than 70 marks in Science.

maths = {Uday, Akshay, Hiral, Alakh, Harsh}
science = {Khushi, Prince, Parth, Uday, Akshay}
class1 = {Uday, Akshay, Hiral, Alakh, Harsh, Khushi, Prince, Parth, Uday, Akshay}
"""

s1 = {1, 13, 24, 56, 13, 44, 66, 78, 87, 31, 13, 20}

# r = s1.pop()
# print(r)

# s1.remove(103)
s1.discard(103)
print(s1)

# tarak maheta, big boss, money highest, asur
"""
ratings = [
    {3, 5, 7, 1},
    {9, 0, 8, 2},
    {11, 5, 3, 8}
]
"""
maths = {"Uday", "Akshay", "Hiral", "Alakh", "Harsh"}
science = {"Khushi", "Prince", "Parth", "Uday", "Akshay"}

# maths.update(science)
# print(maths)

science.update(maths)
print(science)