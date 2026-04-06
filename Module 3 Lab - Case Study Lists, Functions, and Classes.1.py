# Superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Subclass
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__("car")  # Automatically set vehicle type to "car"
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("\nVehicle Information:")
        print(f"  Vehicle type: {self.vehicle_type}")
        print(f"  Year: {self.year}")
        print(f"  Make: {self.make}")
        print(f"  Model: {self.model}")
        print(f"  Number of doors: {self.doors}")
        print(f"  Type of roof: {self.roof}")

# Main program
def main():
    print("Enter details for your car:")

    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")

    # Validate doors input
    while True:
        doors = input("Number of doors (2 or 4): ")
        if doors in ['2', '4']:
            doors = int(doors)
            break
        else:
            print("Please enter 2 or 4.")

    # Validate roof input
    while True:
        roof = input("Type of roof (solid or sun roof): ").lower()
        if roof in ["solid", "sun roof"]:
            break
        else:
            print("Please enter 'solid' or 'sun roof'.")

    # Create Automobile object
    my_car = Automobile(year, make, model, doors, roof)

    # Display car information
    my_car.display_info()

if __name__ == "__main__":
    main()
