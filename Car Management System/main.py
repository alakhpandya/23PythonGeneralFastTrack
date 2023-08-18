from car import Car
from hatchback import HatchBack
from suv import SUV
from sedan import Sedan
from van import Van
from premiumHatchback import PremiumHatchBack
from atv import ATV

h1 = HatchBack("Alto", "CNG", 300000)
sv1 = SUV("Ertiga", "Diesel", 1200000)
sd1 = Sedan("Ciaz", "Petrol", 1000000)
v1 = Van("Eeco", "CNG", 300000)
p1 = PremiumHatchBack("Baleno", "Petrol", 800000)
a1 = ATV("Gipsy", "Petrol", 500000)

# sd1.printDetails()
# sv1.change_seating_capacity(6)
# SUV.change_seating_capacity(6)
# sv1.printDetails()
sv2 = SUV("Breeza", "Diesel", 1000000)
# sv2.printDetails()

while True:
    print("Press:")
    print("1 to add new car")
    print("2 to view details of an existing car")
    print("3 to update details of a car")
    print("4 to delete a car")

    print("9 to exit")
    ch = int(input())

    if ch == 1:
        print("Press:")
        print("1 for Van")
        print("2 for Hatchback")
        print("3 for ATV")
        print("4 for Sedan")
        print("5 for Premium Hatchback")
        print("6 for SUV")
        car_type = int(input())
        create_new_car = {
            1 : Van.addNewCar,
            2 : HatchBack.addNewCar,
            3 : ATV.addNewCar,
            4 : Sedan.addNewCar,
            5 : PremiumHatchBack.addNewCar,
            6 : SUV.addNewCar
        }
        create_new_car[car_type]()


    elif ch == 2:
        c = Car.get_sr_no()
        Car.stock[c].printDetails()
        print()
    
    elif ch == 3:
        pass
    
    elif ch == 4:
        c = Car.get_sr_no()
        removed_car = Car.stock.pop(c)
        print(f"{removed_car.name} has been successfully removed...")
    
    elif ch == 9:
        break

    else:
        print("Invalid option, please try again...\n")