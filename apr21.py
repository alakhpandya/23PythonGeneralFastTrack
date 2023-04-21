
# a = int(input("Enter two numbers:\n"))
# b = int(input())

# Operators in Python:
# Arithmetic Operators:
"""
+, -, *, /, %, // - floor division, ** - power

"""
# print(a / b)
# print(a % b)

"""
days = int(input("Days: "))
# months = days // 30
months = int(days / 30)
print("Answer =", months, "months and ", end = "")
remaining_days = days % 30
print(remaining_days, "days")
"""


"""
floor(-5.9)
ceil(5.1)
ceil(-3.7)
"""
"""
base = int(input("Base: "))
power = int(input("Power: "))
answer = base ** power
print("Answer =", answer)
"""


# Comparision Operators/Relational Operators/Conditional Operators/Conditions

"""
<, >, <=, >=, ==, !=
These operators always returns either True or False.
"""

# print(5 < 10)
# print(10 < 6)
# print(10 <= 10)
"""
a = int(input("No 1: "))
b = int(input("No 2: "))
print(a == b)
"""
"""
password = input("Enter password: ")
correct_password = "maiNahiBataunga"
print(password == correct_password)
"""

# Logical Operators:
"""
and, or, not
"""
"""
correct_userName = "user"
correct_password = "pwd"

user_name = input("User name: ")
password = input("Password: ")

print(user_name == correct_userName and password == correct_password)
"""
"""
required_experience = 5
required_qualification = "MCA"


experience = int(input("Experience: "))
qualification = input("Qualification: ")
criminal_history = int(input("Criminal History(0/1): "))

print((experience >= required_experience or
qualification == required_qualification) and (not criminal_history))
"""

# Assignment Operators: 
"""
a = 5 * 13 + 20 / 2 ** 3 
 <--
B   - Bracket
O   - Of (Power)
D/M - Division/Multiplication
A/S - Addition/Subtraction

a = 5 * 13 + 20 / 2 ** 3 
print(a)
"""

a = 5
b = 15
# a = a + b
a += b   
print(a)

"""
# shorthand operators (Assignment operators)
a = a + b	=>	a += b
a = a - b	=>	a -= b
a = a * b	=>	a *= b
a = a / b	=>	a /= b
a = a % b	=>	a %= b
a = a // b	=>	a //= b
a = a ** b	=>	a **= b
"""
"""
a = 25
b = 7
a **= b
print(a)
"""

# strings in Python - Immutable & Ordered
s1 = 	"Summer is at the peak and swimming pools are overcrowded at the weekends."
# index: 0123456789...............................................................
# -ve in:................................................................987654321
print(s1[7])
# print(s1[700])
print(s1[-3])
print(len(s1))
s2 = "Hello"

