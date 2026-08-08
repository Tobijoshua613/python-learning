# 🧬 Python Inheritance Practice


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} vehicle is starting...")


class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is driving 🚗")


class ElectricCar(Car):
    def charge(self):
        print(f"{self.brand} electric car is charging 🔋")


# Create an electric car
my_car = ElectricCar("Tesla")

# Use methods inherited from parent classes
my_car.start()
my_car.drive()

# Use its own method
my_car.charge()
