# Q - 10:
"""
n = 60
1, 3, 7, 13, 21, 31, 43, 57
  2  4  6  8   10  12  14
next term: 57 (uday)/ 
"""
# Print above series.
"""
n = int(input("n: "))
t = 1
d = 2
while t <= n:
    print(t)
    t = t + d
    d = d + 2
"""

# Take 'n' from user & print all integers from 1 to n.
"""
for n = 6, output should be:
1,
2,
3,
4,
5,
6
"""
"""
n = int(input("n: "))
t = 1
d = 2
terms = []
while t < n:
    terms.append(t)
    t = t + d
    d = d + 2
i = 0
while i < len(terms)-1:
    print(terms[i], end=", ")
    i += 1
print(terms[i])
"""
"""
a = int(input("a: "))
b = int(input("b: "))

num = a
while num <= b:
    o=0
    i=1
    while(i<=num):
        if(num%i==0):
            o+=1   
        i+=1   
    if(o==2):
        print(num)

    num += 1
"""