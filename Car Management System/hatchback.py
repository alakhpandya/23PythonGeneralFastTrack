from car import Car

class HatchBack(Car):
    category = "H"
    def __init__(self, name, fuel, price, AC):
        super().__init__(name, fuel, price)
        self.AC = AC

    def printDetails(self):
        super().printDetails()
        print("AC:", self.AC)

    @classmethod
    def addNewCar(cls):
        name, fuel, price = super().addNewCar()
        AC = input("AC Type: ")
        return cls(name, fuel, price, AC)