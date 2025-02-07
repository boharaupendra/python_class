from re import A
from xml import dom


domain = ['mindriser.com.np', 'nepalgunjcollege.edu.np', 'thapatech.com.np', 'amanboyshostel.com.np',]
print(domain)
print("****** Enetr your email id  ******")
mail = input("Enetr Your Email: ")
if mail.endswith("@gmail.com"):
    print("Email is valid")
else:
    print("Email is invalid")