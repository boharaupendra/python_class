# Encapsulation
# public - can be access throught the system. no symbol before attribute name
# protected - can be access throught the package. single underscore is use before attribute name
# private - can be access only inside the class. double underscore is use before attribute name

class Employee():
    def __init__(self):
        # public properties
        self.name = "Mira"
        self.address = "Dolpa"
        self.designation = "Reception"

        # protected properties
        self._emptype = "Full Time"
        self._shift = "Morning Shift"

        # private properties
        self.__contact = "987641234"
        self.__email = "mira@gmail.com"

    # public method - we can access private properties via public method
    def getContactEmail(self):
        print("Email:", self.__email)
        print("Contact:", self.__contact)    
        
print("Encapsulation")
emp1 = Employee()
# accessing public properties
print("Public Properties")
print("Name:", emp1.name)
print("Address:", emp1.address)
print("Designation:", emp1.designation)
print("")

# accessing protected properties
print("Protected Properties")
print("Employee Type:", emp1._emptype)
print("Shift:", emp1._shift)
print("")

# accessing private properties - we cannot access private properties direct
print("Private Properties")
emp1.getContactEmail()
# print("Contact:", emp1.__contact)
# print("Email:", emp1.__email)
print("")

# storing values in public properties
print("Public Properties")
emp1.name = "Mikasa"
emp1.address = "LOL"
emp1.designation = "Brand Ambassadar"

print("Name:", emp1.name)
print("Address:", emp1.address)
print("Designation:", emp1.designation)
print("")

# storing values in protected properties
print("Protected Properties")
emp1._emptype = "Part Time"
emp1._shift = "Day Shift"

print("Employee Type:", emp1._emptype)
print("Shift:", emp1._shift)
print("")

# storing values in private properties - we cannot store value directly to private properties
print("Private Properties")
emp1.__contact = "47514"
emp1.__email = "mikasa@gmail.com"
emp1.getContactEmail()
# print("Contact:", emp1.__contact)
# print("Email:", emp1.__email)
print("")

# accessing and storing values to private properties through access modifier
# getter and setter method
class Vehicle():
    def __init__(self):
        self.__brand = str
        self.__model = str
        self.__type = str

    def getBrand(self):
        return self.__brand

    def setBrand(self, brand):
        self.__brand = brand

    def getModel(self):
        return self.__model

    def setModel(self, model):
        self.__model = model

    def getType(self):
        return self.__type

    def setType(self, vehtype):
        self.__type = vehtype

    def getInfo(self):
        print("Model:", self.getModel())
        print("Type:", self.getType())

print("")
v1 = Vehicle()
v1.setBrand("Suzuki")
print("Brand:", v1.getBrand())
print("")
v1.setBrand("Mitsubi")
print("Brand:", v1.getBrand())

v1.setModel("Land Rover")
v1.setType("Four Wheel")
v1.getInfo()
