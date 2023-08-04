# Creating class
class Car():
    seats = 5       # class variable

    # Method
    def printDetails(self):
        print("Name:", self.name)
        print("Fuel:", self.fuel)
        print("Price:", self.price)
        print("Seats:", self.seats)
        print()

c1 = Car()
c1.name = "i20"
c1.fuel = "Diesel"
c1.price = 1000000

# print("Name:", c1.name)
# print("Fuel:", c1.fuel)
# print("Price:", c1.price)
# print("Seats:", c1.seats)
# print()
c1.printDetails()

Car.seats = 4

c2 = Car()
c2.name = "BMW G1"
c2.fuel = "Petrol"
c2.price = 5600000

# print("Name:", c2.name)
# print("Fuel:", c2.fuel)
# print("Price:", c2.price)
# print("Seats:", c2.seats)
# print()
c2.printDetails()

c3 = Car()
c3.name = "XUV700"
c3.fuel = "Diesel"
c3.price = 2500000
c3.seats = 7

# print("Name:", c3.name)
# print("Fuel:", c3.fuel)
# print("Price:", c3.price)
# print("Seats:", c3.seats)
# print()
c3.printDetails()

c4 = Car()
c4.name = "Swift"
c4.fuel = "Petrol"
c4.price = 600000

# print("Name:", c4.name)
# print("Fuel:", c4.fuel)
# print("Price:", c4.price)
# print("Seats:", c4.seats)
# print()
c4.printDetails()
