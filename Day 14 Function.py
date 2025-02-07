# Function
# to takes input, processes it and returns output
# to reuse certain block of code
# to execute the function it must be called/invoked by its name

# syntax
# def functionname():
#   block of code

# example
def myInfo():
    print("This is a information about me")
    
myInfo()

def message():
    print("Balen is the newly elected Mayor of Kathmandu Metro Municipality")
message()

def sumOfTwoNum(num_one, num_two):
    result = num_one + num_two
    print("Sum of two number:", result)
sumOfTwoNum(12, 12)
print("")
# parameter - when a variable is defined inside parenthesis and passed while defining
# the function then it is parameter
# argument - when value is passed to the variable while invoking/calling the function
# then it is argument

# Types of function
# 1. with parameter and return type
# 2. with parameter and no return type
# 3. without parameter and return type
# 4. without parameter and no return type

# 1. with parameter and return type
def powerOf(num, power):
    result = num**power
    return result
print("Power of: ",powerOf(2, 5))

print("")
# 2. with parameter and no return type
def bankDetails(bank_name, bank_code):
    print("Bank Name: ", bank_name, " Bank Code: ", bank_code)
bankDetails("Sidhartha Bank", "SDTH2022")
print("")

# 3. without parameter and return type
def getCountryName():
    country = ["Maldives", "Bangladesh", "Nepal", "Bhutan"]
    return country

print("List of countries:", getCountryName())

# 4. without parameter and no return type
def showNumberBetween():
    for i in range(2, 20):
        print("Number:", i)
    else:
        print("Number between: 2-20")
showNumberBetween()

# extra example
users = ["sandesh", "madan", "melina", "mahima", "bhupesh"]

def check_user(user):
    if user in users:
        print("Available")
    else:
        print("User Unavailable")

def check(user):
    for val in users:
        if user == val:
            print("Username exist")
        else:
            print("Username not exist")

def login():
    username = input("Enter your username: ")
    check_user(username)
    check(username)
    
login()



