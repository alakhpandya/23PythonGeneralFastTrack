# Write a program that takes an integer from user and prints number of digits of that integer.
# Decision Making (if-else)
# indentation
"""
a = 5
if (a >= 0){
    printf("Positive");
}
else{
    printf("Negative");
}
printf("End of the program.");

# Output:
Positive
"""
"""
marks = 88
if marks >= 80:
    print("Congratulations, you are amongst the toppers!")
    print("We need party!")
elif marks >= 70:
    print("Pass")
else:
    print("Sorry, you need to attempt again...")
print("End of the program.")
"""
# Shorthand if conditions:
"""
month = int(input("Enter birth-month number: "))
if month == 1: print("January")
elif month == 2: print("February")
elif month == 3: print("March")
elif month == 4: print("April")
elif month == 5: print("May")
elif month == 6: print("June")
elif month == 7: print("July")
elif month == 8: print("August")
elif month == 9: print("September")
elif month == 10: print("October")
elif month == 11: print("November")
elif month == 12: print("December")
else: print("Invalid month number, please enter between 1 to 12.")
"""
"""
marks = 58
print("Congratulations, you are amongst the toppers!") if marks >= 80 else print("Sorry, you need to attempt again...")
print("End of the program.")
"""

# 
"""
PAR: 7
Strokes         Score
1               Hole in One
2 to 4          Eagle
5 or 6          Birdy
7               PAR
8 or 9          Bogey
10              Double Bogey
>10             Go Home


PAR: 10
Strokes         Score
1               Hole in One
2 to 7          Eagle
8 or 9          Birdy
10              PAR
11 or 12        Bogey
13              Double Bogey
>13             Go Home
"""