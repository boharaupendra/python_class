# Break Statement
# to terminate the iteration or loop

odd_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
while count < len(odd_list):
    if odd_list[count] == 5:
        break
    else:
        print("Item: ", odd_list[count])
    count += 1

for i in range(len(odd_list)):
    if i == 6:
        break
    else:
        print(i)

# Continue
# use to skip the rest of the code inside a loop for the current iteration only
name = "Kathmandu"
for char in name:
    if char == "m":
        continue
    elif char == "d":
        break
    else:
        print(char)

# Pass
# Null statement
# python iterpreter do not ignore pass because certain memory is allocated

name = "Pokhara"
for i in name:
    pass

# Primary Number
# is divided by self and one
# modulas
# double for loop


