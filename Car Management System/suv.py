from car import Car

class SUV(Car):
    seats = 7
    category = "S"
    ground_clearance = 170

    def printDetails(self):
        super().printDetails()
        print("Ground Clearance:", self.ground_clearance)

    # static methods: methods those do not use 'self' (Mostly they are called through class, not through objects)
    @staticmethod
    def change_seating_capacity(new_seating_capacity):
        SUV.seats = new_seating_capacity

