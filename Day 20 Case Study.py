# Case Study
# SAARC Countries and their capital
saarc_country_list = ["Nepal", "Bhutan", "Maldives", "Sri Lanka", "India",\
                      "Bangladesh", "Afghanistan", "Pakistan"]

capital_list = [('Nepal', 'Kathmandu'), ('Bhutan', 'Thimpu'),\
                ('Maldives', 'Male'), ('Sri Lanka', 'Colombo'),\
                ('India', 'New Delhi'), ('Bangladesh', 'Dhaka'), \
                ('Afghanistan', 'Kabul'), ('Pakistan', 'Islamabad')]
user_list = [('Admin', 'Admin'), ('User', 'User')]

# message response
def msg(code):
    if code == "LS":
        return "Login Success"
    elif code == "LF":
        return "Login Fail"
    elif code == "NC":
        return "Is not a SAARC Country"
    elif code == "NU":
        return "Is not a valid User Account"
    else:
        return "Try again later"

# checking saarch country
def is_saarc():
    country = input("Enter a saarc country name: ")
    if country in saarc_country_list:
        print("Capital of ", country, " is: ", get_capital(country))
        is_saarc()
    else:
        print(country, msg("NC"))
        is_saarc()

# showing capital city
def get_capital(country):
    for i in range(len(capital_list)):
        data = capital_list[i]
        counter = 1
        for i in range(len(data)):
            if data[i] == country:
                return data[counter]

# checking user
def check_user(user, passcode):
    for i in range(len(user_list)):
        data = user_list[i]
        counter = 0
        for j in range(len(data)):
            if user == data[counter] and passcode == data[counter + 1]:
                return True
        i += 1
# main method
def main():
    user = input("Enter Username: ")
    passcode = input("Enter Passcode: ")
    if check_user(user, passcode) == True:
        print(msg("LS"))
        is_saarc()
    else:
        print(msg("LF"))
        print(msg("NU"))
        main()
main()


