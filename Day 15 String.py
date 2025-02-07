# String
# 1. capitalize() - returns the first character of the string in upper case and other
# in lower case
print("capitalize()")
quote = "Dont BUILD a castle in AIR"
print(quote)
print(quote.capitalize())
print(quote)
print("")

# 2. casefold() - returns all string character in lower case
print("casefold()")
german_word = "Floßes"
print(german_word.casefold())
print("")

# 3. lower() - to convert character string to lowercase
# 4. upper() - to convert character string to uppercase
print("upper() & lower()")
msg = "HELLO WORLD"
response = "hello world"
print(msg, " to lower:", msg.lower())
print(response, " to upper: ", msg.upper())
print("")

# 5. find() - returns the first index number of the string character available in
# the string
quote = "Dont BUILD a castle in AIR"
print("find()")
print("Index of: ", quote.find("I"))
print("")

# 6. count() - returns the total number of string character occurences in the string
quote = "Dont BUILD a castle in AIR"
print("count()")
print("Total: ", quote.count("I"))
print("Total: ", quote.count("a"))
print("Total: ", quote.count(" "))
print("")

# 7. startswith() - returns true if the string starts with specified string
print("startswith()")
name = "Bulbul Pandey"
print(name.startswith("Bul"))
print(name.startswith("bul"))
print("")

# 8. endswith() - returns true if the string ends with specified string
print("endswith()")
email = "sandesh@mindrisers.com.np"
print(email.endswith("com.np")) # true
print(email.endswith("gmail.com")) # false
print("")

# 9. split() - returns the string in list when splited with substring
print("split()")
places_name = "Kathamandu, Pokhara, Butwal, Dhangadi, Lalitpur, Baglung"
result = places_name.split(", ")
print("result:", result)
print("")

# 10. join() - joins the items of the list with the string and returns in string
# syntax
# str.join(list)
print("join()")
result = ['Kathamandu', 'Pokhara', 'Butwal', 'Dhangadi', 'Lalitpur', 'Baglung']
names = ", ".join(result)
print(names)
print("")

# 11. isalnum() - returns true if the string is alphanumeric
print("isalnum()")
password = "sandesh123"
passcode = "dsan@123__123"
print(password.isalnum())
print(passcode.isalnum())
print("")

# 12. isalpha() - returns true if the string is alphabetical character
print("isalpha()")
name = "urbasi"
password = "sandesh123"
passcode = "dsan@123__123"
print(password.isalpha())
print(passcode.isalpha())
print(name.isalpha())
print("")

# 13. format() - formats the value of substitution string
# case one - no index no variable
print("format() case one:")
msg = "Hi {} are you from KTM {}?"
print(msg.format("Binod", 40))
print("")

# case two - only index
print("format() case two:")
msg = "Hi {0} are you from KTM {1}?"
print(msg.format("Harry", 32))
print("")

# case three - only variable
print("format() case three:")
msg = "Hi {name} are you from KTM {ward}?"
print(msg.format(ward=32, name="Mina"))
print(msg.format(name="Sohan", ward=14))
print("")

# case four - with index and variable
print("format() case four:")
msg = "Hi {name} are you from KTM {0}?"
print(msg.format(32, name="Mina"))
print("")

# 14. replace() - replaces the old string with new string
print("replace()")
email = "sandesh@mindrisers.com.np"
print("Old String:", email)
print("New String:", email.replace("sandesh", "muna"))
print("New String:", email.replace("com.np", "org"))
print("")
