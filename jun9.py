# loops:
"""
while loop
for loop
"""
# while loop - when we don't know the exact number of iterations
"""
i = 1    # loop control variable
print("Start of the program.")
while i < 6:
    print(i, "Hello Royal!")
    i += 1
print("End of the program.")
"""
# Class work:
"""
1. Write a program that prints multiplicative table of 7 using while loop.
example:
output:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
..........
7 x 10 = 70

2. Write a program that takes an integer from user & prints its multiplicative table using while loop.
example:
input:
5
output:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
..........
5 x 10 = 50

"""

# Most frequent use of while loop in Python - creating infinite loops
print("Enter two numbers:")
a = float(input())
b = float(input())
while True:
    op = input("Enter operation (+, -, *, / or 'x' to quit): ")
    if op == "+":
        print(f"{a} + {b} = {a + b}")
    elif op == "-":
        print(f"{a} - {b} = {a - b}")
    elif op == "*":
        print(f"{a} * {b} = {a * b}")
    elif op == "/":
        print(f"{a} / {b} = {a / b}")
    elif op == "x":
        break
    else:
        print("Invalid operation, please try again...")
# HW:
"""
1. A school has following grading system. Write a Python code that takes percentage of a student and display his/her grade.
below 35%       :   F
from 35 to 44   :   E
from 45 to 54   :   D
from 55 to 64   :   C
from 65 to 74   :   B
75 or more      :   A

2. Write a Python program to find whether a given year is a leap year or not. 
Test Data : 2016
Expected Output :
2016 is a leap year.

3. Write a Python program to find the largest of three numbers. 
Test Data : 12 25 52
Expected Execution:
1st Number = 12
2nd Number = 25
3rd Number = 52

52 is the largest number.

4. Write a Python program to accept a coordinate point in a XY coordinate system and determine in which quadrant the coordinate point lies. 
Test Data : 
x-coordinate: 7
y-coordinate: 9
Expected Output :
The coordinate point (7,9) lies in the First quadrant.

5. Write a Python program to find the eligibility of admission for a professional course based on the following criteria: 
Eligibility Criteria : 
Marks in Maths must be atleast 65,
Marks in Phy must be atleast 55,
Marks in Chem must be atleast 50 and 
Total marks all three subject must be atleast 190 or Total in Maths and Physics >=140
Input the marks obtained in Mathematics :72 
Input the marks obtained in Physics :65 
Input the marks obtained in Chemistry :51 
Total marks of Maths, Physics and Chemistry : 188 
Total marks of Maths and Physics : 137 
The candidate is not eligible.


6. Take values of length and breadth of a rectangle from user and check if it is square or not.

7. A shop gives discount of 10% if the cost of purchased quantity is more than Rs.1000.
Ask user for quantity
Assume each item costs 100.
Calculate and print total amount to be paid by user.

8. In above program, ask user for his/her name, mobile number, quantity and price of each item, then decide whether he/she is eligible for discount and based on that print the invoice in the following format:
case 1- when customer is not eligible for discount:

------------------------Retail Invoice---------------------
Customer Name: xxxxxx
Contact Number: xxxxxx
Date of Invoice: 09-01-2022
-----------------------------------------------------------
Items               Price       Quantity        Total
item-1              50          3               150
item-2              100         4               400
item-3              40          5               200
                                                ---------
                                Final Amount:   750
----------------Thanks for shopping with us!---------------

case 2- when customer is eligible for discount:

------------------------Retail Invoice---------------------
Customer Name: xxxxxx
Contact Number: xxxxxx
Date of Invoice: 09-01-2022
-----------------------------------------------------------
Items               Price       Quantity        Total
item-1              90          3               270
item-2              100         4               400
item-3              40          10              400
                                                ---------
                                Grand Total:    1070
                                Discount:        107
                                                ---------
                                Final Amount:    963
----------------Thanks for shopping with us!---------------

9. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and years of service and print the final salary.
"""
# While Loop examples:
"""
1. Write a Python code that takes an integer from user and prints number of digits in that integer.
2. Write down a Python code that creates a user defined list
3. Write a Python code to print each of the elements of a given list in a new line
4. Write a Python program that prints whether the number given is a prime number or not.
5. Write a Python program that prints whether the number given is a perfect number or not.
6. Write a Python program that prints whether the number given is an Armstrong number or not.
7. Write a Python program that prints all the prime numbers between two integers given by user.
8. Write a Python program that prints all the perfect numbers between two integers given by user.
9. Write a Python program that prints all the Armstrong numbers between two integers given by user.
10. Ask an integer n from user. Print the following sequence seperated by comma (,) up to n. Make sure your code doesn't print comma after the last number.
	1, 3, 7, 13, 21, 31, 43
"""

