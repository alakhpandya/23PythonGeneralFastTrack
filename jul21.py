# Functions = Assistants
# What we give - argument
# What assistants give us back - return
"""
1. No arguments, no return
2. Takes arguments, no return
3. No arguments, return
4. Takes arguments, return
"""

"""
def junagadhInfo():
    print("Junagadh district is located in western Gujarat and is surrounded by Arabian sea and forest area.\nThe district is divided into 10 talukas of which major ones include, Junagadh, Keshod, Mangrol, Manavadar.\nJunagadh is famous for the Gir Sanctuary, the only abode to Asiatic lions and mountain range of Girnar which is a major pilgrimage destination.\nThe District Comprises within 05 Revenue Sub-Division & 10 Talukas.\n")

a = int(input("Enter two integers:\n"))
b = int(input())

if a - b > 0:
    junagadhInfo()

c = a + b
d = c % 5
if a >= b:
    junagadhInfo()

if a / b > 1:
    junagadhInfo()

if a + b > b:
    junagadhInfo()
"""
'''
def sqrt(n):
    print(f"Square root of {n} = {n ** 0.5}")

"""
5 ** 1/2 = 5 x 5 = 25
5 ** 1/3 = 
"""

# sqrt(36)
# sqrt(1024)
sqrt()
'''
"""
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print("fact=",fact)

def sqrt(n):
    print(f"Square root of {n} = {n ** 0.5}")

# factorial(5)
# factorial(7)
n = int(input("Enter a number: "))  # 5
factorial(n)
"""
"""
def sqrt(n):
    m = n ** 0.5
    print(f"Square root of {n} = {m}")
    return m

a = int(input("Enter two integers:\n")) # 25
b = int(input())    # 16
# output: 9
c = sqrt(a) + sqrt(b)
print(c)
"""

# Take 5 numbers from user and print sum of their factorials on the screen.
"""
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    # print("fact=",fact)
    return fact

a = int(input("Enter 5 integers:\n")) # 8
b = int(input())   # 5
c = int(input())   # 4
d = int(input())   # 5
e = int(input())   # 6
ans = factorial(a) + factorial(b) + factorial(c) + factorial(d) + factorial(e)
print("ans =", ans)
"""

'''
def avg(a, b):
    return (a + b)/2

# Ask two numbers from user and print average of their factorials using avg() and factorial() functions.
"""
x = 5
y = 6

ans = 420
"""
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

x = int(input("Enter 2 integers:\n"))
y = int(input())

a = factorial(x)
b = factorial(y)

ans = avg(a, b)
print(ans)
'''