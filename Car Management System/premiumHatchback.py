from hatchback import HatchBack

class PremiumHatchBack(HatchBack):
    categroy = "P"
    airbags = 4

    def printDetails(self):
        super().printDetails()
        print("Airbags:", self.airbags)

    @classmethod
    def addNewCar(cls):
        return super().addNewCar()