#loop
#to perform certain task repeteately to certain point of time
#for loop
#stright forward loop
#syntax
#for val in sequence:
#   block of code
#example
orders =["momo","slice","samosa ","water"]
for item in orders:
    print (item)
#range ()
#to get int value from two point i.e. starting and end  point
#here starting point is always smaller than end point
    #sntax
    #range(end)-equivalent to range(0,end)
    #reryrn value between 0 to -1
    #values are increment by 1
    #range(start,end)
    #return value between start to end step
    #value are increment by step



#implementing range with for loop
for  i in range (4):
    print ("Index :",i,"item: ",orders[i])
#we can count the size or length of list using len() function
print("method 1")
for  i in range (len(orders)):
    print ("Index :",i,"item: ",orders[i])
#method 2
print("method 2")
count=len(orders)
for  i in range (count):
    print ("Index :",i,"item: ",orders[i])
#implement else with for loop





#advancing for loop using if statement and input

number=(11,22,33,44,55,66,77,88,99,111)
num=int(input("enter number : "))
for check in number:
    if check == num:
        print ("you are luckey")
    else:
        print ("you are not luckey")


        
        
