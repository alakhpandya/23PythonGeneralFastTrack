from car import Car

class ATV(Car):
    category = "A"
    fwd = True

    def printDetails(self):
        super().printDetails()
        print("Four wheel drive:", self.fwd)

