from car import Car

class SUV(Car):
    seats = 7
    category = "S"
    AC = "Front & Rear"

    def __init__(self, name, fuel, price, ground_clearance):
        super().__init__(name, fuel, price)
        self.ground_clearance = ground_clearance

    def printDetails(self):
        super().printDetails()
        print("Ground Clearance:", self.ground_clearance)

    # static methods: methods those do not use 'self' (Mostly they are called through class, not through objects)
    @staticmethod
    def change_seating_capacity(new_seating_capacity):
        SUV.seats = new_seating_capacity

    @classmethod
    def addNewCar(cls):
        name, fuel, price = super().addNewCar()
        ground_clearance = int(input("Ground clearance: "))
        cls(name, fuel, price, ground_clearance)