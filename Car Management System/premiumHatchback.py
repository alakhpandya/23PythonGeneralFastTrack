from hatchback import HatchBack

class PremiumHatchBack(HatchBack):
    categroy = "P"
    airbags = 2
    AC = "Front & Rear"

    def printDetails(self):
        super().printDetails()
        print("Airbags:", self.airbags)

