# 🔄 Python Polymorphism Practice


class Car:
    def move(self):
        print("🚗 Car is driving on the road.")


class Boat:
    def move(self):
        print("🚤 Boat is sailing on the water.")


class Airplane:
    def move(self):
        print("✈️ Airplane is flying in the sky.")


# Create objects
vehicles = [
    Car(),
    Boat(),
    Airplane()
]


# Same method, different behavior
for vehicle in vehicles:
    vehicle.move()
