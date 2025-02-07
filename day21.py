#8 pop()---->remove the random arbitary value from set
item={"key ","locker","box","tool","table"}
print("before",item)
item.pop()
print("after",item)

#discard()-->remove the element from the  set it it is a member otherwise do nothing

item={"key ","locker","box","tool","table"}
print("before",item)
item.discard("bottle")
print("after",item)
item.discard("box")
print("after",item)
#10 remove()-->remove the element from the  set it it is a member otherwise do nothing
item={"key ","locker","box","tool","table"}
print("before",item)
#item.remove("bottle")
item.remove("tool")
print("after",item)
#11 union()--->
print("!!!!!!!!!!!!!!!!union set()!!!!!!!!!!!!!!!!!!!!")
set1={1,2,4,6,8,9}
set2={1,3,4,7,8,9,10}
newset=set1.union(set2)
print(newset)
# 12 update()--->updates the set with item of iterable
print("!!!!!!!!!!!!!!!!update set()!!!!!!!!!!!!!!!!!!!!")
set1={1,2,4,6,8,9}
set2={1,3,4,7,8,9,10}
set1.update(set2)
print(set1)
#print(set2)
#13  isdisjoint()--->check
print("!!!!!!!!!!!!!!!!disjoint set()!!!!!!!!!!!!!!!!!!!!")
set1={1,2,4,6,8,9}
set2={3,5,7}
print (set1.isdisjoint(set2))
print (set2.isdisjoint(set1))
print (set1.isdisjoint(set1))
#issubset()-->
print("!!!!!!!!!!!!!!!!sub set()!!!!!!!!!!!!!!!!!!!!")
set1={1,2,4,6,8,9}
set2={1,2,4}
print (set1.issubset(set2))
print (set2.issubset(set1))
print (set1.issubset(set1))

# 15 superset()--->
print("!!!!!!!!!!!!!!!!super set()!!!!!!!!!!!!!!!!!!!!")
set1={1,2,4,6,8,9}
set2={1,2,4}
print (set1.issuperset(set2))
print (set2.issuperset(set1))
print (set1.issuperset(set1))

#File Handeling
#we have four mode in file handeling
#1 read 'r'
#this mode is used to read the file content and throw error if the file doesnot exit
#file_dir="c:/Users/Dell/Desktop/Python-Cheat-Sheet.doc"
#file =open(file_dir,"r")
#print(file.read())
#file.close()
#2 read line()---->

#file_
#print ("readline()")
#dir="c:\\Users\\Dell\\Desktop\\up.txt"
#file =open(file_dir,"r")
#print(file.readline())
#file.close()
#we can also pass the interer argument in the readline
#reaslines()
#dir="c:\\User\\
#file =open(file_dir,"r")
#print(file.readlines())
#file.close()

#2 append 'a'
#this mode is used to add new content after exiting content of the file content are added from the end of the line of old content and create new file if not exit
print("append()")
file_dire="c:/Users/Dell/Desktop/up.txt"
file=open(file_dire,"a")
file.write(".\n ihfoih uahilfd ")
file.close()
file =open(file_dire,"r")
print(file.read())
file.close()
#3 writ 'w'
# used to add new content in the file
#removes /clear all exting content and add new content in  the file
#create new file if not exit
#
print("!!!!!!!!!!!!!!!!!!write()!!!!!!!!!!!!!!!!!!!")
file_dire="c:/Users/Dell/Desktop/up.txt"
file=open(file_dire,"w")
file.write("hi there how are u living ")
file.write("hi there how are u living in usa man! ")
file.close()
file =open(file_dire,"r")
print(file.read())
file.close()
#########
print("!!!!!!!!!!!!!!!!!!new write()!!!!!!!!!!!!!!!!!!!")
file_dire="c:/Users/Dell/Desktop/up12.txt"
file=open(file_dire,"w")
file.write("hi there how are u living ")
file.write("hi there how are u living in usa man! ")
file.close()
file =open(file_dire,"r")
print(file.read())
file.close()
#create 'x'
()
#########
#print("!!!!!!!!!!!!!!!!!!new write()!!!!!!!!!!!!!!!!!!!")
#file_dire="c:/Users/Dell/Desktop/up22.txt"
#file=open(file_dire,"x")
#file.write("hi there how are u living ")
#file.write("hi there how are u living in usa man! ")
#file.close()
#file =open(file_dire,"r")
#print(file.read())
#file.close()
#######
#print("recreate")

#file_dire="c:/Users/Dell/Desktop/up22.txt"
#file=open(file_dire,"x")
#file.write("hi there how are u living ")
#file.write("hi there how are u living in usa man! ")
#file.close()
##file =open(file_dire,"r")
#print(file.read())
#file.close()
#maka a
#file_dire="c:/Users/Dell/Desktop/list.txt"
#file=open(file_dire,"r")
#print(len(file_dire))

#def checkuser():
   # file_dire="c:/Users/Dell/Desktop/list.txt"
    #file =open(file_dire,"r")
    
    #counter=1
print("2079/2/30")   
#exception handeling--error during run time  of the code or program;
#NameError
#ValueError
#KeyError
 #IndexError
 #overflowerror
 #filenotfounderror
 #syntaxerror
#zeroDivisionerror

 #syntax
#try:
    #block of code
#execpt:
    #block of code



 #example
try:
    name
    print(name)
except:
    print("not correct input plese check input")
#specific exception
try:
    print(100/0)
except:
    print("whole number cannot divide by zero")
#except:
    #print("error raised")

try:
    item=["table","tennis"]
    print(item[5])
except IndexError as e:
    print("error!!!!!!!!!")
#multiple execption error class with their own message
try:
    item=["table","tennis",1,3,5,6,7,8,9]
    print(item[5])
    name
    print(name)
    order=dict()
    order.popitem();
    
except (IndexError, KeyError, NameError) as e:
    print(e)
except:
    print("somethig else")


#finally
try:
    file_dire="c:/Users/Dell/Desktop/up12.txt"
    file=open(file_dire,"r")
    print(file.read())
except FileNotFound as e:
    print(error)
except:
    print("read complete")
    print("begin")
    file.close()
    print("file closed")
    
    





























