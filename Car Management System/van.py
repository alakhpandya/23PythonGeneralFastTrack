from car import Car

class Van(Car):
    seats = 9
    category = "V"

    def __init__(self, name, fuel, price, registration_type):
        super().__init__(name, fuel, price)
        self.registration_type = registration_type

    def printDetails(self):
        super().printDetails()

    @classmethod
    def addNewCar(cls):
        name, fuel, price = super().addNewCar()
        registration_type = input("Registration type: ")
        return cls(name, fuel, price, registration_type)