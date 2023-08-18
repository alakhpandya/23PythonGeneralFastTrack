from car import Car

class ATV(Car):
    category = "A"
    def __init__(self, name, fuel, price, fwd):
        super().__init__(name, fuel, price)
        self.fwd = fwd

    def printDetails(self):
        super().printDetails()
        print("Four wheel drive:", self.fwd)

    @classmethod
    def addNewCar(cls):
        name, fuel, price = super().addNewCar()
        fwd = bool(input("Four wheel drive (True/False): "))
        return cls(name, fuel, price, fwd)