from enum import Enum

# --- Enumerations ---
class FuelType(Enum):
    GASOLINE = "Gasoline"
    BIOETHANOL = "Bioethanol"
    DIESEL = "Diesel"
    BIODIESEL = "Biodiesel"
    NATURAL_GAS = "Natural Gas"

class VehicleType(Enum):
    CITY_CAR = "City Car"
    SUBCOMPACT = "Subcompact"
    COMPACT = "Compact"
    FAMILY = "Family"
    EXECUTIVE = "Executive"
    SUV = "SUV"

class Color(Enum):
    WHITE = "White"
    BLACK = "Black"
    RED = "Red"
    ORANGE = "Orange"
    YELLOW = "Yellow"
    GREEN = "Green"
    BLUE = "Blue"
    VIOLET = "Violet"

# --- Main Class ---
class Vehicle:
    def __init__(self, brand, year, motor, fuel_type, vehicle_type, doors, seats, max_speed, color):
        self.brand = brand
        self.year = year
        self.motor = motor
        self.fuel_type = fuel_type
        self.vehicle_type = vehicle_type
        self.doors = doors
        self.seats = seats
        self.max_speed = max_speed
        self.color = color
        self.current_speed = 0

    # Getters
    def get_brand(self): return self.brand
    def get_year(self): return self.year
    def get_motor(self): return self.motor
    def get_current_speed(self): return self.current_speed

    # Setters
    def set_brand(self, brand): self.brand = brand
    def set_current_speed(self, speed): self.current_speed = speed

    # Action Methods
    def accelerate(self, amount):
        if self.current_speed + amount > self.max_speed:
            print("Warning: Max speed exceeded!")
        else:
            self.current_speed += amount
        print(f"Current speed: {self.current_speed} km/h")

    def decelerate(self, amount):
        if self.current_speed - amount < 0:
            print("Warning: Speed cannot be negative!")
        else:
            self.current_speed -= amount
        print(f"Current speed: {self.current_speed} km/h")

    def brake(self):
        self.current_speed = 0
        print("Vehicle stopped. Speed: 0 km/h")

    def get_travel_time(self, distance):
        if self.current_speed == 0:
            return 0
        return distance / self.current_speed

    def print_details(self):
        print("\n--- VEHICLE DETAILS ---")
        print(f"Brand: {self.brand} | Year: {self.year} | Motor: {self.motor}L")
        print(f"Type: {self.vehicle_type.value} | Fuel: {self.fuel_type.value}")
        print(f"Color: {self.color.value} | Speed: {self.current_speed} km/h")

# --- User Input & Execution ---
print("--- Enter Vehicle Information ---")
b = input("Brand: ")
y = int(input("Year: "))
m = float(input("Motor Capacity (L): "))
d = int(input("Doors: "))
s = int(input("Seats: "))
ms = int(input("Max Speed: "))

# Object creation
my_car = Vehicle(b, y, m, FuelType.GASOLINE, VehicleType.COMPACT, d, s, ms, Color.WHITE)

# Simulation required by the book
my_car.set_current_speed(100)
my_car.accelerate(20)
my_car.decelerate(50)
my_car.brake()
my_car.print_details()