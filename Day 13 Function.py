# Function - takes input, processes it and returns output
# to re-use certain block of code to perform certain task with same
# purpose

# syntax
# def <function_name>():
#   block of code

# example
def day_name():
    print("Today is Thursday")

# we must call a function by its name in order to execute the code
day_name()
print("")
# parameters and arguments in function
# parameter -> varaible that is passed inside parenthesis while
# defining the function

# argument -> value that is passed inside parenthesis when the
# function is being called

# example
# here number_one and number two are parameters and are treated as
# local variable inside that particular function that they are
# being passed

def sumOfTwoNumber(number_one, number_two):
    result = number_one + number_two
    print("Sum: ", result)
    
# here 45 and 77 two are arguments
sumOfTwoNumber(45, 77)
print("")
# Types of function
# 1. with parameter and return type
# 2. with parameter and no return type
# 3. without parameter and return type
# 4. without parameter and no return type

# 1. with parameter and return type
def powerOf(number, power):
    result = number**power
    return result
# we must print the function if it is a return type
print(powerOf(3, 5))
print("")
# 2. with parameter and no return type
def capitalName(capital):
    if capital == "Kathmandu":
        print(capital, " is the capital of Nepal")
    elif capital == "Delhi":
        print(capital, " is the capital of India")
    elif capital == "Thimpu":
        print(capital, " is the capital of Bhutan")
    else:
        print(capital, " is the capital of some country")

capitalName("Kathmandu")
capitalName("Delhi")
capitalName("Thimpu")
print("")

# 3. without parameter and return type
def valueOfPi():
    pi = 22/7
    return pi

print("Value of Pi is:", valueOfPi())
print("")
def getAddressDetails():
    list_of_address = ["Kathmandu", "Pokhara", "Bhaktapur"]
    return list_of_address

print("Address List: ", getAddressDetails())
print("")
# 4. without parameter and no return type
def employeeAndDesignation():
    emp_details = {"name":"Manoj Tripathi", "designation":"MD"}
    print("Details:", emp_details)
employeeAndDesignation()
print("")

def charactersAndActor():
    details = {"character":"Vasme Don", "actor":"Bipin Karki"}
    print("Details:", details)
charactersAndActor()

# TASK Day 13
# Make Three Function
# 1. Message Response Function according to CODE passed and return
# message

# 2. Takes Username and Password and Confirms Login Credentials and
#  returns true or false accordingly

# 3. Login functions takes Username and Password Input
# and checks Username and Password using number 2 function
# if response is true call Message Response function with Success Code
# if response is false call message response function with fail code

