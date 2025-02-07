# Input - Output
# output -> print() 

# we use input() function to take certain input from the use
# by default -> the value of that input() returns is str

# example
name = input("Enter your name: ")
print(type(name))
print(name)

# int/float input from the user
# we have to do type casting
# two ways
# method one:- direct in input function - recommended
number_one = int(input("Enter first number: "))

# method two:- after taking input
number_two = input("Enter second number: ")

sum = number_one + int(number_two)
print("Sum of two number is: ", sum)

# mini price calculator
quantity = int(input("Total number of quantity: "))
price = float(input("Enter the price: "))
discount = float(input("Discount: "))

total_price = (quantity * price)
discount_price = total_price * (discount/100)
grand_total = total_price - discount_price
print("Your grand total: ", grand_total)

# if elif statement + nested if statement implementation
# student's position marking system
std_reg_number = "STD2022002"
std_login_code = "LG2022"

print("*** Welcome to MindRisers | Student Portal ***")
print("Please enter the required field to log-into the system")
input_regno = input("Enter your registration number: ")
# identity operator will not work in this case because
# identity operator checks whether the two objects are pointing to
# same reference in the memory or not
# in this case 'input_regno' value is dynamic and reference is also
# dynamic

if input_regno == std_reg_number:
    input_login_code = input("Enter passcode: ")
    if input_login_code == std_login_code:
        print("Login Success")
        obtained_marks = float(input("Enter your obtained marks: "))
        if obtained_marks >= 0 and obtained_marks <= 39.99:
            print("Fail")
        elif obtained_marks >= 40 and obtained_marks <= 59.99:
            print("Third Division")
        elif obtained_marks >= 60 and obtained_marks <= 69.99:
            print("Second Division")
        elif obtained_marks >= 70 and obtained_marks <= 84.99:
            print("First Division")
        elif obtained_marks >= 85 and obtained_marks <= 100:
            print("Distinction")
        else:
            if obtained_marks < 0 or obtained_marks > 100:
                print("Please enter the number between 0-100")
            else:
                print("Enter numeric value")
    else:
        print("Invalid Registration No or Passcode")
else:
    print("Not registered yet")

# Import
# to include any module/package/library in our program
# we always place import code at the begining of the program
# we use import
# from
# syntax
# from <package_name> import <module_name>

import math

print(math.factorial(5))


