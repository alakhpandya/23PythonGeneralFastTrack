class Car():
    stock = []
    seats = 5       # class variable

    def __init__(self, name, fuel, price):
        self.name = name
        self.fuel = fuel
        self.price = price
        Car.stock.append(self)

    # Method
    def printDetails(self):
        print("Name:", self.name)
        print("Fuel:", self.fuel)
        print("Price:", self.price)
        print("Seats:", self.seats)
        
    @staticmethod
    def get_sr_no():
        print("---------Cars in stock----------")
        print("Sr.No.\tModel Name")
        for car in Car.stock:
            print(f"{Car.stock.index(car)}\t{car.name}")
        c = int(input("Sr no: "))
        return c

class SUV(Car):
    seats = 7
    category = "S"
    ground_clearance = 170

    def printDetails(self):
        super().printDetails()
        print("Ground Clearance:", self.ground_clearance)
        print()

    # static methods: methods those do not use 'self' (Mostly they are called through class, not through objects)
    @staticmethod
    def change_seating_capacity(new_seating_capacity):
        SUV.seats = new_seating_capacity

class Sedan(Car):
    category = "L"

class HatchBack(Car):
    category = "H"
    AC = "front"
    fwd = False

class Van(Car):
    seats = 9
    category = "V"

class PremiumHatchBack(HatchBack):
    categroy = "P"

class ATV(Car):
    category = "A"

h1 = HatchBack("Alto", "CNG", 300000)
sv1 = SUV("Ertiga", "Diesel", 1200000)
sd1 = Sedan("Ciaz", "Petrol", 1000000)
v1 = Van("Eeco", "CNG", 300000)
p1 = PremiumHatchBack("Baleno", "Petrol", 800000)
a1 = ATV("Gipsy", "Petrol", 500000)

# sd1.printDetails()
# sv1.change_seating_capacity(6)
# SUV.change_seating_capacity(6)
# sv1.printDetails()
sv2 = SUV("Breeza", "Diesel", 1000000)
# sv2.printDetails()

while True:
    print("Press:")
    print("1 to add new car")
    print("2 to view details of an existing car")
    print("3 to update details of a car")
    print("4 to delete a car")

    print("9 to exit")
    ch = int(input())

    if ch == 1:
        pass

    elif ch == 2:
        c = Car.get_sr_no()
        Car.stock[c].printDetails()
    
    elif ch == 3:
        pass
    
    elif ch == 4:
        c = Car.get_sr_no()
        removed_car = Car.stock.pop(c)
        print(f"{removed_car.name} has been successfully removed...")
    
    elif ch == 9:
        break

    else:
        print("Invalid option, please try again...\n")