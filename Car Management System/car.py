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
        print("Category:", self.category)
        print("Fuel:", self.fuel)
        print("Price:", self.price)
        print("Seats:", self.seats)
        
    @staticmethod
    def get_sr_no():
        if not Car.stock:
            print("There is no car in the stock at present!")
            return False
        print("---------Cars in stock----------")
        print("Sr.No.\tModel Name")
        for car in Car.stock:
            print(f"{Car.stock.index(car)}\t{car.name}")
        c = int(input("Sr no: ")) + 1
        return c

    @staticmethod
    def addNewCar():
        print("Enter the following details:")
        name = input("Name: ")
        fuel = input("Fuel: ")
        price = int(input("Price: "))
        return name, fuel, price