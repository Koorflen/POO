import math

# --- Class Circle ---
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.PI * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * math.PI * self.radius

# --- Class Rectangle ---
class Rectangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return self.base * self.height

    def get_perimeter(self):
        return (2 * self.base) + (2 * self.height)

# --- Class Square ---
class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return 4 * self.side

# --- Class Right Triangle ---
class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return (self.base * self.height) / 2

    def get_perimeter(self):
        return self.base + self.height + self.get_hypotenuse()

    def get_hypotenuse(self):
        return math.sqrt((self.base ** 2) + (self.height ** 2))

    def get_triangle_type(self):
        hypotenuse = self.get_hypotenuse()
        if self.base == self.height == hypotenuse:
            return "Equilateral"
        elif self.base != self.height and self.base != hypotenuse and self.height != hypotenuse:
            return "Escalene"
        else:
            return "Isosceles"

# --- MAIN EXECUTION --- 
print("--- Geometric Shapes Calculator ---")

# Circle Input
r = float(input("Enter Circle radius (cm): "))
my_circle = Circle(r)

# Rectangle Input
rb = float(input("Enter Rectangle base (cm): "))
rh = float(input("Enter Rectangle height (cm): "))
my_rectangle = Rectangle(rb, rh)

# Square Input
s = float(input("Enter Square side (cm): "))
my_square = Square(s)

# Triangle Input
tb = float(input("Enter Triangle base (cm): "))
th = float(input("Enter Triangle height (cm): "))
my_triangle = RightTriangle(tb, th)

# Printing Results
print("\n--- RESULTS ---")
print(f"Circle: Area = {my_circle.get_area():.2f}, Perimeter = {my_circle.get_perimeter():.2f}")
print(f"Rectangle: Area = {my_rectangle.get_area():.2f}, Perimeter = {my_rectangle.get_perimeter():.2f}")
print(f"Square: Area = {my_square.get_area():.2f}, Perimeter = {my_square.get_perimeter():.2f}")
print(f"Triangle: Area = {my_triangle.get_area():.2f}, Perimeter = {my_triangle.get_perimeter():.2f}")
print(f"Triangle Hypotenuse: {my_triangle.get_hypotenuse():.2f}")
print(f"Triangle Type: {my_triangle.get_triangle_type()}")