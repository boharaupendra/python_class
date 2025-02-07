email_domain=["@gmail.com","@outlook.com","@yahoo.com","@AOL.com","@hotmail.com","@protonmail.com"]
global count_one
global count_two
def getEmail():
    input_email=input("Enter your email address")
    return input_email

def emailValidation():
    email=getEmail()
    for i in range(0, len(email_domain)):
        domain= email.endswith(email_domain[i])
        if domain==True:
            count_one=1
        elif domain==False:
            count_two=0
        else:
            pass
    if count_one==1:
        print("Email is valid")
    elif count_two==0:
        print("Email is invalid")
    else:
        pass

    
emailValidation()
