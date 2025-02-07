# Encapsulation
# public - no symble before attribute name
# protected - single underscore before attribute name
# private - double underscore before attribute name

class Employee():
    def __init__(self):
        # public properties
        self.name = "Ram Narayan"
        self.address = "Bhaktapur"
        self.designation = "Managing Director"

        # protected properties
        self._dob = "2000-02-12"
        self._emp_type = "Full Time"

        # private properties
        self.__email = "rn@gmail.com"
        self.__contact = "977-9876543210"

    def getEmailAndContact(self):
        print("Email:", self.__email)
        print("Contact:", self.__contact)

emp1 = Employee()
# accessing public properties
print("Public Properties")
print(emp1.name)
print(emp1.address)
print("")

# accessing protected properties
print("Protected Properties")
print(emp1._dob)
print(emp1._emp_type)
print("")

# accessing private properties
print("Private Properties")
# print(emp1.__email)
# print(emp1.__contact)
emp1.getEmailAndContact()
print("")

# we cannot access private protected/private properties direct so in order to access we should use public
# method or we can implement access modifier
# similarly we cannot store value as well

# storing public properties
print("Public Properties")
emp1.name = "Hari Prasad"
emp1.address = "Kalanki"
print(emp1.name)
print(emp1.address)
print("")

# storing protected properties
print("Protected Properties")
emp1._dob = "1996-12-15"
emp1._emp_type = "Part Time"
print(emp1._dob)
print(emp1._emp_type)
print("")

# storing private properties
print("Private Properties")
emp1.__email = "hp@gmail.com"
emp1.__contact = "983165745"
# print(emp1.__email)
# print(emp1.__contact)
emp1.getEmailAndContact()
print("")

# access modifier - accessing and storing values in private properties using getter and setter method
class Person():
    def __init__(self):
        self.__gender = str
        self.__stage = str

    def getGender(self):
        return self.__gender

    def setGender(self, gender):
        self.__gender = gender

    def getStage(self):
        return self.__stage

    def setStage(self, stage):
        self.__stage = stage

    def getPersonDetail(self):
        print("Gender:", self.getGender())
        print("Stage:", self.getStage())

p1 = Person()
p1.setGender("Male")
p1.setStage("Adult")
print("Gender:", p1.getGender())
print("Stage:", p1.getStage())

p1.getPersonDetail()
    


    
    
