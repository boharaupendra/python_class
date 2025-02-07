# scenario/concept - mini atm authentication system 1. checking balance
# Account Holder - AC Number, Pin Code
# Available Balance - Check

# system analysis and implementation
# Account Holder
account_holder = ["AC100", "AC101", "AC102"]

# Account Holder Pin Code
account_pincode = [("AC100", 1234), ("AC101", 2244),("AC102", 1122)]

# account holder's available balance
account_balance = {
    "AC100": 5000.00,
    "AC101": 2000.00,
    "AC102": 9000.00
    }

# system CLI design and implementation
print("*** MIND Risers MINI ATM ***")
print("Enter Account Number: ")

# taking input from user
# static account number as input
user_ac = "AC101"

# checking account number
# in real world scenario - account number is already decode inside atm card so
# we dont have to input account number but in our case we dont have card so we
# are asking account number as input from user

# membership operator - in, not in
# if statement - this logic will not work for us in this particular scenario
# if user_ac in account_holder:
#     print("Account Available")

# if else statement
if user_ac not in account_holder:
    print("Your account number is invalid.")
else:
    # if account number is valid then we should ask for pin code
    print("Enter Your Pin Code: ")
    pin_code = 2244
    # if pin code is true
    # but we must be sure that the account number and pincode must be of same
    # account number
    # so that we are checking available pincode and account number in 'tuple'
    # with 'and' operator because 'and' operator checks that all conditions must be true
    if pin_code in account_pincode[0] and user_ac in account_pincode[0]:
        # account_pincode[0] = ("AC100", 1234)
        # pin_code = 2244
        # user_ac = "AC101"
        
        # 2244 in ("AC100", 1234) first condition false so will not check another condition
        print("*** Welcome: 1 - ", user_ac, " ***")
        print("*** Your available balance is: ", account_balance['AC100'])
    elif pin_code in account_pincode[1] and user_ac in account_pincode[1]:
        # account_pincode[1] = ("AC101", 2244)
        # pin_code = 2244
        # user_ac = "AC101"
        
        # 2244 in ("AC101", 2244) first condition true so will check second condition
        # "AC101" in ("AC101", 2244) second condition true
        
        # here both condition are true so our code will execute further in this section
        print("Welcome: 2 - ", user_ac)
        print("*** Your available balance is: ", account_balance['AC101'])
    elif pin_code in account_pincode[2] and user_ac in account_pincode[2]:
        print("Welcome: 3 - ", user_ac)
        print("*** Your available balance is: ", account_balance['AC102'])
    else:
        print("Invalid Pincode")
    
