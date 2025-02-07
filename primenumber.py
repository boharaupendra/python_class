num = int(input("enter the number: "))
if num<2:
    print(num,"is not prime number")
else:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not prime number")
            break
    else:
        print(num,"is prime number")
        