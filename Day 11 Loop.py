# Loop 
# to perform certain task repeatedly to certain point of time

# for loop
# straight forward loop
# syntax

# here val is an identifier so we can keep any possible name for it

# for val in sequence:
#   block of code

# example
orders = ["Momo", "Cold Drinks", "Samosa", "Water"]

for item in orders:
    print(item)

# Range()
# to get int value from two point i.e starting and end point
# here starting point is always smaller than end point

# syntax
# range(end) - equivalent to range(0, end)
# returns value between 0 to (end -1)
# values are increment by 1

# range(start, end)
# returns value between start to end-1
# values are increment by 1

# range(start, end, step)
# returns value between start to end-step
# values are increment by step

# example
print("Range")
print("Range:", *range(10))
print("Range:", *range(2, 20))
print("Range:", *range(3, 21, 3))
print("")
# implementing range with for loop
orders = ["Momo", "Cold Drinks", "Samosa", "Water"]
# displaying with hard code
print(orders[0])
print(orders[1])
print(orders[2])
print(orders[3])

# displaying with dynamic using loop
for i in range(4):
    print("Index: ", i, " Item: ", orders[i])
print("")
# we can count the size or length of list using len() function
print("Length of List: ", len(orders))
print("")

# we can use this value in two ways
# method one:- direct passing to range()
for i in range(len(orders)):
    print("Index: ", i, " Item: ", orders[i])
print("")

# method two:- storing to variable and using it via reference
count = len(orders)
for i in range(count):
    print("Index: ", i, " Item: ", orders[i])
print("")

# implementing else with for loop
number = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for num in number:
    print("Number: ", num)
else:
    print("No more numbers")

# advancing for loop using if statement and input

number = (11, 22, 33, 44, 55, 66, 77, 88, 99)

num = int(input("Enter number: "))

for check in number:
    if check == num:
        print("You're lucky")
    else:
        print("You're Unlucky")

num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for val in num_list:
    if val%2 == 0:
        print(val, " is divided by 2")
    else:
        print(val, " is not divisible by 2")

for i in range(len(num_list)):
    if i == 3:
        for j in range(i):
            print(j)
        else:
            print("Completed task for", i)
    else:
        print(i)




