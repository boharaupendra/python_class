# Decorator - to add extra functionality to a function

def addTwo(a, b):
    return a + b

sumTwo = addTwo(2, 5)
print(addTwo(3, 5))

del addTwo
print(sumTwo)

#addTwo(3, 5)

def showMsg():
    print("Hello world")

msg = showMsg()
msg
# del showMsg

# function inside function i.e inner function
def showMessage():
    message = "Hello"
    def quote(message):
        print(message)
        print("It is a inner function")
    return quote(message)

@showMessage
def decorateMe():
    print("Hello I am decorating")

decorateMe
