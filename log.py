db_username = "lokendra"
db_password = "lok123"
username = input("Enter your username: ")
if db_username == username :
    print("Now enter your password ")
    password = input("Enter your password: ")
else:
    print("Your email or password is invalid")
if db_password == password:
    name = input("Enter Your name: ")
    print("Welcome to result Session ",name)
    print("Now check your Result")
    marks = float(input("Enter your marks: "))
#for Division
    total_marks = float(input("Enetr Total marks: "))
    percentage = marks/total_marks*100
    Gpa = marks/total_marks*4
    if percentage <= 39 and percentage >= 0:
        print("Sorry ",name,"You are fail")
        print("your percentage is:",percentage)
    elif percentage <= 49 and percentage >= 40:
        print("Congratulation",name,"You getThird division")
        print("your percentage is:",percentage)
    elif percentage <= 59 and percentage >= 50:
        print("Congratulation",name,"You getSecond Division")
        print("your percentage is:",percentage)
    elif percentage <= 79 and percentage >=60:
        print("Congratulation",name,"You get First Division")
        print("your percentage is:",percentage)
    elif percentage <= 100 and percentage >=80:
        print("Congratulation",name,"You get Distriction")
        print("your percentage is:",percentage)
    else:
        print("This marks is not included in system")
#for grading
    if percentage>=90 and percentage<=100:
        print("Your GPA is A+")
        print("Your GPA point is :",Gpa)
    elif percentage>=80 and percentage<=89:
        print("Your GPA is A")
        print("Your GPA point is :",Gpa)
    elif percentage>=70 and percentage<=79:
        print("Your GPA is B+")
        print("Your GPA point is :",Gpa)
    elif percentage>=60 and percentage<=69:
        print("Your GPA is B")
        print("Your GPA point is :",Gpa)
    elif percentage>=50 and percentage<=59:
        print("Your GPA is C+")
        print("Your GPA point is :",Gpa)
    elif percentage>=40 and percentage<=49:
        print("Your GPA is C")
        print("Your GPA point is :",Gpa)
    elif percentage>=30 and percentage<=39:
        print("Your GPA is D+")
        print("Your GPA point is :",Gpa)
    elif percentage>=20 and percentage<=29:
        print("Your GPA is D")
        print("Your GPA point is :",Gpa)
    elif percentage>=10 and percentage<=19:
        print("Your GPA is E+")
        print("Your GPA point is :",Gpa)
    elif percentage>=0 and percentage<=9:
        print("Your GPA is E")
        print("Your GPA point is :",Gpa)
    else:
        print("This marks is not included in system")
else:
    print("Your email or password is invalid")
