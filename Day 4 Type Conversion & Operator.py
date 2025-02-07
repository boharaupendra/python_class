# Type Conversion or Type Casting
# to convert one datatype into another datatype

# Cases why converting datatype
# int -> float, str
# float -> int, str
# str -> float, int depends upon the data it is carrying

# int - int()
num = int(200.99)
print(type(num))
print(num)

result = 123332.12311
print(type(result))

res = int(result)
print("result", res)
print(type(res))


# str to int
name = "Dharara123"
number = "123"
# if only numbers then converted into int otherwise will not convert

converted_number = int(number)
print(type(converted_number))
print("Number:", number)

#converted_name = int(name)
#print(type(converted_name))
#print("Name:", converted_name)

# int and str to float
# float()
num_test = 123 # it is a int value
numbers = "1235" # it is a str value with numbers only
names = "Kathmandu123123" # it is a str value with numbers and letters

# int to float converted easily
int_float = float(num_test)
print(type(int_float))

# str with numbers only converted easily
str_float_only_numbers = float(numbers)
print(type(str_float_only_numbers))

# str with numbers and letters do not convert
# str_alpha_numeric = float(names)
# print(type(str_alpha_numeric))

# int and float to str - can be easily converted in any of the case
num_int = 123123123
num_float = 123.1222

int_str = str(num_int)
print(type(int_str))
print(int_str)
float_str = str(num_float)
print(type(float_str))
print(float_str)

# set to list and list to set
item_list = ["books", "boots", "planes", "Copters"]
item_set = {"Pencil", "Box", "Stitch", "Tools"}

# list to set
converted_list = set(item_list)
print(type(converted_list))
print(converted_list)

converted_set = list(item_set)
print(type(converted_set))
print(converted_set)

# cannot converted to dict so need to be cautious

# Operator - to operate certain operation in the program
# Types of operator
# 1. Arithmetic Operator 
# 2. Assignment Operator
# 3. Comparative Operator
# 4. Logical Operator # logic gate
# 5. Identity Operator
# 6. Membership Operator
# 7. Bitwise Operator

# Day 4 Task - do research and write down notes (one paragraph)
# binary system
# modulas, floor division, exponent
# logic gate
# test - all datatypes to convert into each datatypes list, set, tuple
# and dict


gender = ("Male", "Female", "Others")
gender_list = list(gender)
print(gender_list)
print(type(gender_list))

day_list = ["Sunday", "Monday"]
day_tuple = tuple(day_list)
print(day_tuple)
print(type(day_tuple))



