from car import Car

class HatchBack(Car):
    category = "H"
    AC = "front"
    fwd = False

    def printDetails(self):
        super().printDetails()
        print("AC:", self.AC)

