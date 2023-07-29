# lambda functions
"""
def sqrt(n):
    return n ** 0.5
"""
# sqrt = lambda n : n ** 0.5
# print(sqrt(81))

"""
def avg(a, b):
    return (a + b)/2
"""
# avg = lambda a, b : (a + b)/2
# print(avg(12, 24))


"""
def junagadhInfo():
    print("Junagadh district is located in western Gujarat and is surrounded by Arabian sea and forest area.\nThe district is divided into 10 talukas of which major ones include, Junagadh, Keshod, Mangrol, Manavadar.\nJunagadh is famous for the Gir Sanctuary, the only abode to Asiatic lions and mountain range of Girnar which is a major pilgrimage destination.\nThe District Comprises within 05 Revenue Sub-Division & 10 Talukas.\n")
"""
# junagadhInfo = lambda : print("Junagadh district is located in western Gujarat and is surrounded by Arabian sea and forest area.\nThe district is divided into 10 talukas of which major ones include, Junagadh, Keshod, Mangrol, Manavadar.\nJunagadh is famous for the Gir Sanctuary, the only abode to Asiatic lions and mountain range of Girnar which is a major pilgrimage destination.\nThe District Comprises within 05 Revenue Sub-Division & 10 Talukas.\n")

# junagadhInfo()

# Built in functions of Python

# sum
"""
# n = [23, 11, 5, -30, 4, 66, 8]
# n = (23, 11, 5, -30, 4, 66, 8)
n = {23, 11, 5, -30, 4, 66, 8}
total = sum(n)
print(total)
"""

# absolute
"""
a = -5
b = 7
print(abs(a))
print(abs(b))
"""

# all & any
"""
print(all([5 > 3, 6 > 4, True]))
print(all([5 > 3, 6 < 4, True]))
print(any([5 < 3, 6 < 4, True]))
print(any([5 < 3, 6 < 4, False]))
"""

# chr : from ASCII to Character
"""
print(chr(65))
"""

# ord: from character to ASCII
"""
print(ord("A"))
"""

# Evaluate
"""
eval("print('Hello World')")
"""

# isinstance
"""
a = 7
print(isinstance(a, int))
print(isinstance(a, float))
print(isinstance(a, str))
"""

# min & max
"""
n = [23, 11, 5, -30, 4, 66, 8]
print(max(n))
print(min(n))
"""

# round
"""
pi = 3.141596
print(round(pi))
a = 31.58
print(round(a))
print(round(pi, 2))
print(round(pi, 3))
"""

# floor & ceil
"""
import math

pi = 3.141596
a = 31.98
b = -2.78

# print(math.floor(pi))
# print(math.floor(a))
# print(math.floor(b))
# print(int(b))

print(math.ceil(pi))
print(math.ceil(a))
print(math.ceil(b))
"""

# zip
"""
letters = ["a", "b", "c", "d"]
numbers = [1, 2, 3, 4]
caps = ("P", "Q", "R", "S")
result = list(zip(letters, numbers, caps))
print(result)
"""
# map, filter

# Q-1:
"""
def sqrt(n):
    return n ** 0.5

n = [23, 11, 5, -30, 4, 66, 8]
# Create another list named as 'roots' containing square roots of the members of n. Use sqrt function.
"""
# def sqrt(n):
#     return n ** 0.5

n = [23, 11, 5, -30, 4, 66, 8]
# roots = []
# for x in n:
#     roots.append(sqrt(x))

# roots = list(map(sqrt, n))
# print(roots)

# roots = list(map(lambda n : n ** 0.5, n))
# print(roots)

# Q-2: First, find the average temperature using avg() function and call it 'average'. Next, use above_avg() function and create a new list named 'high_temp' containing only those temperatures which are more than average temperature.
"""
def avg(x):
    return sum(x)/len(x)

def above_avg(n):
    return n > average

temperatures = [23, 11, 5, -30, 4, 66, 8]
average = avg(temperatures)

# print(average)
# print(above_avg(11))
high_temp = []
for x in temperatures:
    if above_avg(x) == True:
        high_temp.append(x)
print(high_temp)
"""
"""
def avg(x):
    return sum(x)/len(x)

def above_avg(n):
    return n > average

temperatures = [23, 11, 5, -30, 4, 66, 8]
average = avg(temperatures)

# high_temp = list(filter(above_avg, temperatures))
high_temp = list(filter(lambda x : x > average, temperatures))
print(high_temp)
"""

# OOPs in Python