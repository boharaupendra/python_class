# String continue
# replace() - replaces the old string with new string
# takes two parameter 1. old string 2. new string
param = "the world is so compact if we think it as deep"
new_string = "so beautiful"
print("Old String:", param)
result = param.replace("so compact", new_string)
print("New String:", result)
print("")

# isalpha() - returns true if the string is alphabetical string
name = "Kathmandu"
password = "KathM@ndu123__"
print(name.isalpha())
print(password.isalpha())
print("")

# isalnum() - returns true if the string is alpha-numerical string
name = "Kathmandu"
password = "KathM@ndu123__"
passcode = "pass123"
print(name.isalnum())
print(password.isalnum())
print(passcode.isalnum())
print("")

# format() - formats the string substitution
# case one - no index and no variable
message = "Hello {},How are you?You are suppose to come at {} right?"
print(message.format("Jill", 12))
print("")

# case two - with index
message = "Hello {0},How are you?You are suppose to come at {1} right?"
print(message.format("Phill", 1))
print("")

# case three - with variable
message = "Hello {name},How are you?You are suppose to come at {time} right?"
print(message.format(name="Jack", time=5))
print("")

# case four - with index and variable
message = "Hello {name},How are you?You are suppose to come at {0} right?"
print(message.format(5, name="Jack"))
print("")

# find() - returns lowest/first index number of the string/substring/
# character available in the string
quote = "Life is beautiful"
print(quote.find("i"))
print("")

# index() -  - returns lowest/first index number of the string/substring/
# character available in the string
quote = "Life is beautiful"
print(quote.index("i"))
print("")
