# Iterator - is a object that iterates upon self
# 1. iter() or __iter__() - use to create iterator object
# 2. next() or __next__() - goes manually through each iteration and gets the value of object

orders = ["Cover", "Pin", "Comb", "Hairbin", "Cap"]
for val in orders:
    print(val)

# creating iterator object
# iter() - takes iterable object as parameter
obj_one = iter(orders)

print(obj_one)
print(id(obj_one))
print("")

# __iter__() - is called via iterable object
obj_two = orders.__iter__()
print(obj_two)
print(id(obj_two))
print("")

# accessing values of iterator object
# next() - takes iterator object as parameter
print(next(obj_one))
print(next(obj_one))
print(next(obj_one))
print(next(obj_one))
print(next(obj_one))
print("")
# if the item is not available then raise StopIteration exception

# __next__() - is called via iterator object
print(obj_two.__next__())
print(obj_two.__next__())
print(obj_two.__next__())
print(obj_two.__next__())
print(obj_two.__next__())
print("")

# Breaking down for loop
places = ["Kathmandu", "Delhi", "Jakarta", "Maldives", "Bhutan"]
for val in places:
    print(val)

# step one:- iterator object of sequence/iterable is created 
iter_obj = iter(places)

# step two:- infinite while loop is executed to get the value of iterator object
while True:
    try:
        element = next(iter_obj)
        print(element)
    except StopIteration as error:
        print(error)
        break

# it seems like for loop is a infinite while loop in python

# Task try to create our custom iteratable and implement iterator, loop to get values
    
