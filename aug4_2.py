"""
class Car():
    seats = 5       # class variable

    def __init__(self, name, fuel, price):
        self.name = name
        self.fuel = fuel
        self.price = price

    # Method
    def printDetails(self):
        print("Name:", self.name)
        print("Fuel:", self.fuel)
        print("Price:", self.price)
        print("Seats:", self.seats)
        print()
        
class SUV(Car):
    seats = 7
    
c1 = Car("i20", "Diesel", 1000000)
c2 = Car("BMW G1", "Petrol", 5600000)
c3 = SUV("XUV700", "Diesel", 2500000)
# c3.seats = 7
c4 = Car("Swift", "Petrol", 600000)
c5 = Car("Tata Nexon", "Electric", 1800000)
c1.printDetails()
# c2.printDetails()
c3.printDetails()
# c4.printDetails()
# c5.printDetails()

# print(c1.__dict__)
# print(c3.__dict__)
s2 = SUV("Ertiga", "CNG", 1200000)
s2.seats = 6
s2.printDetails()
"""
# 4 pillars of OOP: Inheritance, Abstraction, Encapsulation, Polymorphism

# Inheritance: Single/Simple inheritance

class Father():
    profession = "Business"

class Child1(Father):
    vehicle = "Car"
    profession = "CA"

c1 = Child1()
print(c1.profession)

class GrandChild(Child1):
    profession = "Software Developer"

class Mother():
    hobby = "Swimming"
    profession = "Doctor"

class Class1(Father, Mother):
    pass

class Class2(Mother, Father):
    pass

# class Class3(Class1, Class2):
#     pass
    
"""
f1 = Father()
print(f1.profession)

c1 = Child1()
c1.profession = "Doctor"
print(c1.profession)

gc1 = GrandChild()
print(gc1.profession)

print(gc1.vehicle)
"""

# cl1 = Class1()
# print(cl1.profession)
# print(cl1.hobby)

# cl2 = Class2()
# print(cl2.profession)
# print(cl2.hobby)

# cl3 = Class3()
# print(cl3.profession)


# Next Class: Hierarchical, Multi level & Multiple inheritance and further