# Vehicle Showroom Management System

class Vehicle:
    def __init__(self, vehicle_number, brand, price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price

    def get_category(self):
        if self.price >= 1000000:
            return "Luxury"
        else:
            return "Economy"

    def display(self):
        print("Vehicle Number :", self.vehicle_number)
        print("Brand          :", self.brand)
        print("Price          : ₹", self.price)
        print("Category       :", self.get_category())
        print("-" * 40)


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print("Vehicle added successfully!\n")

    def display_vehicles(self):
        if not self.vehicles:
            print("No vehicles available.")
        else:
            print("\n--- Vehicle Information ---")
            for vehicle in self.vehicles:
                vehicle.display()


# Main Program
showroom = Showroom()

while True:
    print("\n===== Vehicle Showroom Management System =====")
    print("1. Add Vehicle")
    print("2. Display All Vehicles")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        vehicle_number = input("Enter Vehicle Number: ")
        brand = input("Enter Brand: ")
        price = float(input("Enter Price: ₹"))

        vehicle = Vehicle(vehicle_number, brand, price)
        showroom.add_vehicle(vehicle)

    elif choice == "2":
        showroom.display_vehicles()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")
