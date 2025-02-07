# String - method of str
# 1. capitalize - returns the first character str as upper case and
# remaining all in lower case
msg = "hELLo! how you doING?"
print(msg.capitalize())
print("")

# 2. casefold() - returns all string in lower case. Mostly use to
# convert some unicode characters
check = "Floß, das ~ (HolzfloßFlöße)"
print(check.casefold())
print("")
# 3. lower() - returns all string characters in lower case/small letter
# 4. upper() - returns all string characters in upper case/capital letter
# example
# lower
my_msg = "YOU TOLD ME I was not there to him right?"
print(my_msg.lower())
print("")
quote = "Dont build a castle in air"
print(quote.upper())

# 5. count() - returns the total number of str character/sub string
# available in the string
# sub-string -> piece of string which is a part from the string
quote = "Dont build a castle in air"
print(quote.count("D"))
print(quote.count("i"))
print(quote.count(" "))
print(quote.count("ild")) # here 'ild' is a substring
print("")

# 6. startswith() -> returns true if the string starts with particular
# character/sub string
email = "dav@edu.com.np"
print(email.startswith("dav"))

# 7. endswith() -> returns true if the string ends with particular
# character/sub string
email = "dav@edu.com.np"
print(email.endswith("com.np"))
print("")

# 8. split() - breaks the string into multiple pieces with the str
# character or substring and returns them in list
# passed substring is not included in the result
message = "A friend in need is a friend indeed"
result = message.split(" ")
result_two = message.split("end")
print(result)
print(result_two)
print("")

# 9. join() - returns the string with the available items of list
# that are joined by substring
# syntax
# str.join(list)
# " ".join([])
result = ['A', 'friend', 'in', 'need', 'is', 'a', 'friend', 'indeed']
# method one - passing direct
old_string = " ".join(result)
print(old_string)
print("")
# method two - defining variable
ss = " "
new_string = ss.join(result)
print(new_string)
