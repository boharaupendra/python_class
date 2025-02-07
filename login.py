print("***Welcome to Mind-Risers***")
account_status = input('''Press 1 to Login
Don't have a account? Type 2 to SignUP:- ''')
user_names = ["anjal niroula"]
passwords = ["123"]
if account_status == "1":
    user_name = input("Enter your username:- ")
    if user_name in user_names:
        password = input("Enter Your Password:- ")
    else:
        print("***Username not found*** Please signUp new account.")
    if password in passwords:
        print("***Welcome to Mind Risers***")
    else:
        print("User name or password did not match")
else:
    new_user = input("Enter new user name:- ")
    user_names.append(new_user)
    new_password = input("Enter new password")
    passwords.append(new_password)
    print("New user successfully registered")

