# While Loop
# iterates over a block of code as long as the condition is true

# syntax
# while condition:
#   block of code

# example ONE
num = 23
while num == 23:
    print("Do iterate")
    num += 1 # num = 23 + 1 = 24
print("")

# example TWO
sum = 0
i = 1

while i < 10:
    sum = sum + i
    i = i + 1
    print("Sum: ", sum)
    print(i)
print("Total Sum:", sum)
print("")

# example THREE
count = 0
while count < 23:
    print(count)
    count += 1
print("")

# example FOUR
count = 0
while count < 23:
    if count%2 == 0:
        print(count, " is an even number")
    elif count%2 == 1:
        print(count, " is an odd number")
    count += 1
print("")

# implementing else with while loop
orders = ["Phone", "Phone Cover", "Bag", "Lipstick", "Makeup Kit"]
count = 0
while count < len(orders):
    print("Index: ", count, "Item: ", orders[count])
    count = count + 1
else:
    print("No more item")



