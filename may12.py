# Collections in Python
"""
list        Ordered     Mutable
tuple       Ordered     Immutable
set         Unordered   Mutable
frozensets  Unordered   Immutable

string: Ordered & Immutable collection of characters
dictionary: Unordered & Mutable collection of key:value pairs
"""

# list: Ordered & Mutable collection of members
# l1 =    [12, 34, 54, 99.8, -23.45, 100000000, "Ahmedabad", "Junagadh", "Surat"]
# index:  0   1   2    3      4         5           6           7           8

# print(l1)
# print(len(l1))

# n1 = [12, 34, 54, 99.8, -23.45, 100000000, 34, -10.55, -89, 34, 75, 34]

# Accessing through index:
"""
print(n1[3])
print(n1[-5])
n2 = n1[3:9]
print(n2)
print(n1)
"""
# No function changes the original list.

# print(max(n1))
# print(min(n1))
# print(sorted(n1))
# print(n1)

# s1 = "Uday Balas"
# print(sorted(s1))

# cities = ["ahmedabad", "12", "junagadh", "surat", "vadodara", "jamnagar", "jamkhambhalia", "surendranagar", "rajkot", "Vapi"]
# print(sorted(cities))

# List methods:

# n1 = [12, 34, 54, 99.8, -23.45, 100000000, 34, -10.55, -89, 34, 75, 34]

# n1.append(1000)
# print(n1)

# n1.clear()
# print(n1)

# del n1
# print(n1)

# del n1[5]
# print(n1)

# n2 = n1.copy()
# print(n2)

# n2 = n1.count(34)
# print(n1)
# print(n2)

# print(len(n1))

# n2 = [1,2,3,4]
# n1.extend(n2)

# print(len(n1))
# print(n1)

# print(n1.index(-10.55))
# print(n1.index(34))
# print(n1.index(34, 2))

n1 = [12, 34, 54, 99.8, -23.45, 100000000, 34, -10.55, -89, 34, 75, 34]

# n1.insert(4, -900)
# print(n1)

# del n1[6]
# print(n1.pop(6))
# print(n1)

# n1.remove(-89)
# n1.remove(34)
# print(n1)

# n1.reverse()
# print(n1)

n1.sort()
print(n1)
