# File Handling
"""
f = open('ourBatch.csv')
# print(f.read())
data = f.read()
print(data)
f.close()
"""
# File Handling, Error Handling & Resource Management
"""
f = open('ourBatch.csv', "r")    # default: read mode

# print(f.readline())
# print(f.readline())
# print(f.readline())

# data = f.readlines()
# print(data)
# print(data[0])

f.close()
"""
"""
f = open("yourBatch.csv", "w")

f.write("Sr.No.,Faculty,Subject,Rating\n")
data = ["1,Dhiraj,Java,5\n", "2,Tejas,DSA,4.5\n", "3,Rahul,CPP,4\n", "4,Samir,DJANGO,4.5\n"]
f.writelines(data)

f.close()
"""
"""
f = open("yourBatch.csv", "a")
f.write("5,Madhusudan,SQL,5\n")
f.close()
"""
"""
f = open("yourBatch.csv", "a+")

# f.write("6,Krutarth,Python,4\n")
f.seek(0)
print(f.read())

f.close()
"""

# Resource Management
# f = open("yourBatch.csv", "r")
"""
with open("yourBatch.csv", "r") as f:
    data = f.readlines()
    print("-------------------------")
    print("\tHere's the data")
    print("-------------------------")
    for row in data:
        print(row, end="")
"""

# Error handling/Exception handling

# try:
#     print(a/b)
# except:
#     print("Something went wrong please try again")

while True:
    a = int(input("a: "))
    b = int(input("b: "))
    op = input("Operation (+, -, *, / or 'x' to exit): ")
    if op == "+":
        print(f"{a} + {b} = {a + b}")
    elif op == "-":
        print(f"{a} - {b} = {a - b}")
    elif op == "*":
        print(f"{a} * {b} = {a * b}")
    elif op == "/":
        try:
            print(f"{a} / {b} = {a / b}")
        except Exception as e:
            print(e)
    elif op == "x":
        break   
    else:
        print("Invalid input, try again...")