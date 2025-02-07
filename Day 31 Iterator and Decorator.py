# Iterator - is an object that iterates upon self

places = ["Kathmandu", "Pokhara", "Butwal", "Dharan"]
for val in places:
    print(val)
print("")

# methods in iterators
# iter() or __iter__() - creates an iterator object
# next() or __next__() - go manually through each iteration and returns
# the value of iterator object

# creating iterator object
# iter() - takes iterable as argument and creates iterator object
print("object one")
obj_one = iter(places)
print(obj_one)
print(id(obj_one))
print("")

# __iter__() - is called/invoked via iterable object
print("object two")
obj_two = places.__iter__()
print(obj_two)
print(id(obj_two))
print("")

# next() - takes iterator object as argument and returns value
print("value:", next(obj_one))
print("value:", next(obj_one))
print("value:", next(obj_one))
print("value:", next(obj_one))
print("")

# __next__() - is called/invoked via iterator object
print("value:", obj_two.__next__())
print("value:", obj_two.__next__())
print("value:", obj_two.__next__())
print("value:", obj_two.__next__())
print("")

# Try to create iterator object of tuple and display value of tuple

# breaking down for loop
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday")
for i in range(len(days)):
    print("Index:", i, " Value:", days[i])
else:
    print("No more item")
print("")

# step 1 :- iterator object of iterable object is created
iter_obj = iter(days)

# step 2:- infinite while loop is executed
while True:
    try:
        element = next(iter_obj)
        print("Value:", element)
    except StopIteration as error:
        print(error)
        break
# it seems like for loop is an infinite while loop

# creating our own custom iterator and iterable object

class PowerOf:
    '''class to implement an iterator for power of any number'''
    # constructor
    def __init__(self, num, max=0):
        self.num = num
        self.max = max

    def __iter__(self):
        self.num_of_iter = 0
        return self

    def __next__(self):
        if self.num_of_iter <= self.max:
            result = self.num**self.num_of_iter
            self.num_of_iter += 1
            return result
        else:
            raise StopIteration
    
power = PowerOf(3, 5)
print(power)
print(id(power))
# creating iterator object
iter_obj = iter(power)

# displaying value
print("Value:", next(iter_obj))
print("Value:", next(iter_obj))
print("Value:", next(iter_obj))
print("Value:", next(iter_obj))
print("Value:", next(iter_obj))
print("Value:", next(iter_obj))

# implementing for loop

for val in power:
    print(val)
else:
    print("No more item")
print("")

iter_obj = iter(power)
while True:
    try:
        element = next(iter_obj)
        print(element)
    except StopIteration as error:
        print(error)
        break

print("")

    

