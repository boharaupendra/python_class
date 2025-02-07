# Polymorphism with Method overriding
class Vehicle():
    def __init__(self):
        self.vehicle_type = str
        self.brand = str
        self.category = str

    def brake(self):
        print("The vehicle will stop")

    def axcelerate(self):
        print("Axcelerate of Vehicle")
    
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.brand = "Lamborgini"
        self.category = "Light Weight"
        self.vehicle_type = "Four Wheel"

    def brake(self):
        print("Breaking system in car is different")
        print("Braking system mechanism is also different")

class Bike(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.brand = "Bajaj"
        self.category = "Light"
        self.vehicle_type = "Two Wheel"

    def brake(self):
        print("Braking system in bike")

b1 = Bike()
b1.brake()
print(b1.brand)
b1.axcelerate()
print("")

c1 = Car()
c1.brake()
print(c1.brand)
c1.axcelerate()

# Task 1 - Calculate the Area, Perimeter of different shapes implementing
# method overriding

# single inheritance
# multiple inheritance
class Area():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculateArea(self):
        print("Modify me")

class Perimeter():
    def calculatePerimeter(self):
        print("Modify me")

class Square(Area, Perimeter):
    def __init__(self, length):
        Area.__init__(self, length, length)
        self.length = length

    def calculateArea(self):
        print("Area of square:", self.length * self.breadth)

    def calculatePerimeter(self):
        print("Perimeter of square:", 4 * self.length)

class IsoscelesTriangle(Area, Perimeter):
    def __init__(self, length, base, height):
        Area.__init__(self, length, base)
        self.length = length
        self.base = base
        self.height = height

    def calculateArea(self):
        print("Area of triangle:", 1/2* self.base * self.height)

    def calculatePerimeter(self):
        print("Perimeter of triangle:", 2 * self.length + self.base)

sq = Square(4)
sq.calculateArea()
sq.calculatePerimeter()
print("")
it = IsoscelesTriangle(4, 5, 7)
it.calculateArea()
it.calculatePerimeter()

