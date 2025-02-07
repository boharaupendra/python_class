# Tuple
# 1. count() - returns the total number of value/item/element available
days = ("Sunday", "Monday", "Tuesday", "Sunday")
print("count()")
print("Sunday:", days.count("Sunday"))
print("Monday:", days.count("Monday"))
print("Saturday:", days.count("Saturday"))
print("")

# 2. index() - returns the index number of the value available in the tuple

days = ("Sunday", "Monday", "Tuesday", "Sunday")
print("index()")
print("Sunday:", days.index("Sunday"))
print("Monday:", days.index("Monday"))
print("")

# if not available will raise ValueError: tuple.index(x): x not in tuple
# print("Saturday:", days.index("Saturday"))
