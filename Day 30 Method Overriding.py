# Method Overriding
# redefining the base class function's name in child class
# and the purpose of function might be different

class Vehicle():
    def brake(self):
        print("My job is to stop a vehicle")

    def vehicleInfo(self):
        print("This is a vehicle information")

class Bike(Vehicle):
    def brake(self):
        print("I am a abs braking system")
        print("My job is to control vehicle while stoping")

class Car(Vehicle):
    def brake(self):
        print("I am a disk with suspension braking system")
        print("My work is to stop a car")

b1 = Bike()
b1.brake()
b1.vehicleInfo()
print("")

c1 = Car()
c1.brake()
c1.vehicleInfo()

# Task
# Area and Perimeter of different shapes using method
# overriding

# single inheritance
# multiple inheritance
class Area():
    def calculateArea(self):
        print("Please modify me")

class Perimeter():
    def calculatePerimeter(self):
        print("Please modify me")

class Rectangle(Area, Perimeter):
    def __init__(self, length, breadth):
        self.area_result = 0.00
        self.perimeter_result = 0.00
        self.length = length
        self.breadth = breadth

    def calculateArea(self):
        self.area_result = self.length * self.breadth
        return self.area_result

    def calculatePerimeter(self):
        self.perimeter_result = 2 * (self.length + self.breadth)
        return self.perimeter_result

class Triangle(Area, Perimeter):
    def __init__(self, right, left, base, height):
        self.area_result = 0.00
        self.perimeter_result = 0.00
        self.right = right
        self.left = left
        self.base = base
        self.height = height

    def calculateArea(self):
        self.area_result = 1/2*self.base * self.height
        return self.area_result

    def calculatePerimeter(self):
        self.perimeter_result = self.base + self.right + self.left
        return self.perimeter_result
    
print("Rectangle")
rect = Rectangle(12, 16)
print("Area of Rectangle:", rect.calculateArea())
print("Perimeter of Rectangle:", rect.calculatePerimeter())
print("")

print("Triangle")
t1 = Triangle(4, 6, 8, 7)
print("Area of Triangle:", t1.calculateArea())
print("Perimeter of Triangle:", t1.calculatePerimeter())
print("")

        

