# Dict
# 1. clear() - removes all items from the dict
orders = {
    "ID": 12,
    "name":"Prashanna",
    "date": "2022-02-23",
    "item":"Banner"
    }
customers = {
    "name": "Prashanna",
    "contact":"97564584",
    "email":"prashanna@gmail.com"
    }
print("clear()")
print("Before:", orders)
print("Before:", customers)
orders.clear()
customers.clear()
print("After:", orders)
print("After:", customers)
print("")

# 2. copy() - copies all items from one dict to another dict
orders = {
    "ID": 12,
    "name":"Prashanna",
    "date": "2022-02-23",
    "item":"Banner"
    }
customers = {
    "name": "Prashanna",
    "contact":"97564584",
    "email":"prashanna@gmail.com"
    }
print("copy()")
print("orders:", orders)
print("customers:", customers)
new_orders = orders.copy()
visiters = customers.copy()
print("new_orders:", new_orders)
print("visiters:", visiters)
print("")
