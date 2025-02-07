#set -->collection of sequence of undecorated data
#same as list
#mutable
#syntax
#<var_name>={"item1","item2",......,"item n"}
#example
fruit={"banana ","apple","dragon fruits"}
print(fruit)
#list




#tuple-->immutable
#same as list

#syntax
#<var_name>=tuple()
#<var_name>=("item 1","item 2",........"item n")
#<var_name>="item 1","item 2","item 3"...."item n"
#example days , gender,months,
gender=("male","female","others")
print(gender)
print (type(gender))
#special case
name1="sandesh"#string
name2="upendra",#touple
name3=("kathmandu")#string
name4=("pokhara",)#tuple

print(" ")
print(type(name1))
print(type(name2))
print(type(name3))
print(type(name4))
#dict-->key-value pair
#key are unique
#syntx
#<var_name>={"key1":"value1","key2":"value2","key3":"value3",........,"key n":"value n"}
#we can use both single and double quote to wrap the key-value
#example
ordered_item={
    "id":12,
    "item":"tool box",
    "price":1200,
    "ordered_by":"upendra"
    }
print(ordered_item)
print (type(ordered_item))
#line continition '\'-->to continue all line

