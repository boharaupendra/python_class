# Loop
# to perform certain task repeatedly for a period of time or
# until the statement is true

# for loop
# straigh forward loop
# works until it meets the end point of the loop

# syntax
# for val in sequence:
#   expression

# example
items = ["Apple", "Marsi", "Bottle", "Blanket", "Table"]
for val in items:
    print(val)

# range()
# to get int value from the start-end point
# syntax
# 1. range(end) - equivalent to range(0, end)
# output-> 0 to end-1
# 2. range(start, end)
# output-> start to end-1
# 3. range(start, end, step)
# output-> start to end-step

# example
print(range(10)) # range(0, 10)
print(*range(10))

print(*range(2, 23))
print(*range(3, 20, 3))
print(*range(3, 30, 5))

# implementing range in for loop
for i in range(10):
    print(i)

items = ["Apple", "Marsi", "Bottle", "Blanket", "Table", "Tools"]
# displaying list value with index
for i in range(6):
    print("Index: ", i, " Item: ", items[i])
print("")

# counting the length or size of list using len() function
print(len(items))

print("")
# two ways to pass len() value
# one :- direct
for i in range(len(items)):
    print("Index: ", i, " Item: ", items[i])
print("")

# two :- storing to variable
count = len(items)
for i in range(count):
    print("Index: ", i, " Item: ", items[i])
print("")
# implementing else with for loop
for i in range(len(items)):
    print("Index: ", i, " Item: ", items[i])
else:
    print("No more items")

# advancing for loop with if statement
for item in items:
    if item == "Bottle":
        print(item, " is available in the list")
    else:
        print("Available items: ", item)

for i in range(10):
    if i == 2:
        i += 3
        print(i)
    else:
        print(i)
        
# Task for Today:- Check whether the number is prime or not
# using for loop, if condition, operator


