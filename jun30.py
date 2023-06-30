maths = {"Uday", "Akshay", "Hiral", "Alakh", "Harsh"}
science = {"Khushi", "Prince", "Parth", "Uday", "Akshay"}
programming = {"Khushi", "Prince", "Dhiraj", "Krutarth"}
classroom = {"Uday", "Akshay", "Hiral", "Alakh", "Harsh", "Khushi", "Prince", "Parth", "Dhiraj", "Dishant", "Krutarth", "Kunika"}

# s1 = maths.union(science)
# print(s1)

# s2 = science.union(programming)
# print(s2)

# maths.update(science)

# inter = maths.intersection(science)
# print(inter)

# maths.intersection_update(science)

# diff1 = maths.difference(science)       # {"Hiral", "Alakh", "Harsh"}
# print(diff1)

# diff2 = science.difference(maths)       # {"Khushi", "Prince", "Parth"}
# print(diff2)

# maths.difference_update(science)

# s = diff1.union(diff2)
# print(s)

# s = maths.symmetric_difference(science)     # (maths - science) U (science - maths)
# print(s)

# s2 = science.symmetric_difference(maths)    # (science - maths) U (maths - science)
# print(s2)

# science.symmetric_difference_update(maths)

print(maths.isdisjoint(programming))
print(programming.issubset(classroom))
print(classroom.issuperset(programming))