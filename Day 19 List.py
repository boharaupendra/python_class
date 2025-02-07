# List
# 1. append() - adds the item (object) at the last index of list
animal_list = ["Tiger", "Lion"]
print("append()")
print("Animal Before:", animal_list)
animal_list.append("Bear")
animal_list.append("Jaguar")
print("Animal After:", animal_list)
print("")

# 2. copy() - copies all items from primary list to another list
animal_list_copied = animal_list.copy()
print("copy()")
print("Copied:", animal_list_copied)
print("")
# if we add items to primary list after copying the items to another
# list then they will be no impact on the copied list
print("Animal Before:", animal_list)
print("Copied Before:", animal_list_copied)
animal_list.append("Pangolier")
animal_list.append("Ant Eater")
print("Copied After:", animal_list_copied)
print("Animal After:", animal_list)
print("")

# 3. clear() - removes all items from the list
print("clear()")
print("Copied Before:", animal_list_copied)
animal_list_copied.clear()
print("Copied After:", animal_list_copied)
print("")

# 4. count() - returns the total number of occurences of the value available in
# the list
print("count()")
name_list = ["Mohan", "Lila", "Ram", "Jyoti", "Madan", "Madan", "Min Kumar"]
print("Total:", name_list.count("Madan"))
print("Total:", name_list.count("Jyoti"))
print("")

# 5. extend() - extend the primary list with the items of iterable and append them
# in the primary list
print("extend()")
place_list = ["Pokhara", "Lalitpur"]
city_list = ["Dharan", "Biratnagar", "Butwal"]
print("Place Before:", place_list)
print("City Before:", city_list)
place_list.extend(city_list)
print("Place After:", place_list)
print("City After:", city_list)
print("")

# 6. index() - returns the index number of the value available in the list
print("index()")
print("Place List:", place_list)
print("Index of Dharan", place_list.index("Dharan"))
print("Index of Biratnagar", place_list.index("Biratnagar"))
print("Index of Pokhara", place_list.index("Pokhara"))
print("")

# 7. insert() - takes two parameter
# 1. index number
# 2. value/item
# adds the value/item in the specified index number that we pass as parameter
print("insert()")
item_list = ["Book", "Pen", "Pencil"]
print("Items Before:", item_list)
item_list.insert(1, "Bag")
print("Items After:", item_list)
print("")

# 8. pop() - removes the item from the specified index number
# pop() default - here no index number is passed and it takes -1 as default
# parameter and removes the last index item
print("pop()")
print("Items Before:", item_list)
item_list.pop()
print("Items After:", item_list)
print("")
# pop(index) - here index number is passed and removes the item from the index
# number that is passed
print("pop(index)")
print("Items Before:", item_list)
item_list.pop(0)
print("Items After:", item_list)
print("")

# if the list is empty then IndexError Exception is raised
# odd = list()
# odd.pop()
# odd.pop(1)



