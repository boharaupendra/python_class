# Scenario - Voter Name List Check
# Voter Name
# Voter Card Number
# Citizenship Number

# Request, Process and Final
# Status
# Request List
# Processing List
# Final List

# voter details
voter_one = {"name": "Mina", "citizenship": "C001", "vc": None, "status": "Processing"}
voter_two = {"name": "Muna", "citizenship": "C002", "vc": None, "status": "Request"}
voter_three = {"name": "Parash", "citizenship": "C003", "vc": "VC001", "status": "Final"}

# voter list
voter_list = [voter_one, voter_two, voter_three]

# Business Logic
print("*** Welcome to MIND RISERS Election Comittee ***")
print("Enter your citizenship number: ")

# currently we have static data so we are passing static data to citizenship number
citizenship_number = "C002"

# extracting voter list
print("Loading.......")

# first we need to make sure that the citizenship is registered or not
# P.S: cc -> citizenship_condition
cc_one = voter_list[0]
# here cc_one = {"name": "Mina", "citizenship": "C001", "vc": None, "status": "Processing"}

cc_two = voter_list[1]
# here cc_two = {"name": "Muna", "citizenship": "C002", "vc": None, "status": "Request"}

cc_three = voter_list[2]
# here cc_three = {"name": "Parash", "citizenship": "C003", "vc": "VC001", "status": "Final"}

if cc_one['citizenship'] == citizenship_number:
    # cc_one['citizenship'] = "C001"
    # citizenship_number = "C002"
    # if cc_one['citizenship'] == citizenship_number:
    # if "C001" == "C002"
    print("Found One")
    status = cc_one['status']
    print("Your voter card status is: ", status)

    if status == 'Final':
        print("Your Voter Card Number is: ", cc_one['vc'])
    
elif cc_two['citizenship'] == citizenship_number:
    # cc_two['citizenship'] = "C002"
    # citizenship_number = "C002"
    # if cc_one['citizenship'] == citizenship_number:
    # if "C002" == "C002"
    print("Found Two")
    status = cc_two['status']
    print("Your voter card status is: ", status)

    # cc_two['status'] = "None"
    # if status == 'Final'
    # "None" == "Final" - is false
    if status == 'Final':
        print("Your Voter Card Number is: ", cc_two['vc'])
    
elif cc_three['citizenship'] == citizenship_number:
    print("Found Three")
    status = cc_three['status']
    print("Your voter card status is: ", status)
    
    if status == 'Final':
        print("Your Voter Card Number is: ", cc_three['vc'])
else:
    print("Citizenshp Number Not registered yet")



