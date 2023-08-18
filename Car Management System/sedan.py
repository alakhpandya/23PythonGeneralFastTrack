from car import Car

class Sedan(Car):
    category = "L"
    airbags = 4

    def printDetails(self):
        super().printDetails()
        print("Airbags:", self.airbags)
