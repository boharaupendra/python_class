# Input and Output
# output -> print()
# example
print("This is a output")

# input -> input()
# we use this method to take input from the user
# user inputs from input() method are always string

# example
number_one = input("Enter first number: ")
print(type(number_one))
print(number_one)

# we must type cast or convert into our specific datatype we want
# we can type cast in two ways
# method one -> at the time of input
num = int(input("Enter you number: "))
print(type(num))
print(num)

# method two -> after storing the value
number = input("Enter number: ")
print(int(number))

# asking for string
name = input("Enter your name: ")
address = input("Enter your address: ")
print("Name: ", name, " Address: ", address)

# trying to solve mini login system
db_username = "mindriser"
db_password = "mind123"


# nested if statement
input_username = input("Enter your Username: ")
if input_username == db_username:
    input_password = input("Enter your password: ")
    if input_password == db_password:
        print("*** Welcome to Mind Risers ***")
    else:
        print("Invalid Username or Password")
        # BruteForce Attack
        # Dictioinary Attack
else:
    print("Not registered yet")

# if elif statement example integrating user position marking system
input_username = input("Enter your Username: ")
if input_username == db_username:
    input_password = input("Enter your password: ")
    if input_password == db_password:
        print("*** Welcome to Mind Risers ***")
        # integrating position marking system
        print("*** Enter your obtain marks in order to check your position ***")
        obtained_marks = float(input("Enter your obtained marks: "))
        if obtained_marks >= 0 and obtained_marks <= 39.99:
            print("You are fail")
        elif obtained_marks >= 40 and obtained_marks <= 59.99:
            print("Third Division")
        elif obtained_marks >= 60 and obtained_marks <= 69.99:
            print("Second Division")
        elif obtained_marks >= 70 and obtained_marks <= 84.99:
            print("First Division")
        elif obtained_marks >= 85 and obtained_marks <= 100:
            print("Distinction")
        else:
            print("Enter number between 0-100")
            print("You might not attend the exam. Kindly inform the administration")        
    else:
        print("Invalid Username or Password")
        # BruteForce Attack
        # Dictioinary Attack
else:
    print("Not registered yet")

# import
# to include or import any python package or modules or libraries
# import keyword is use to import pacakges/modules/libraries

# note:- we use import code at the begining of the program
# namespace -> we use namespace of the package/moduel/library name while calling/importing them
# namespace -> it is a unique identifier of the package that its defined particularly somewhere
# in the library

# import module_name
import math

# from package_name import module_name
print(math.factorial(4))



