# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Day1
num1 =10
num2 = 5.2
result = False
num3='xyz'
print(type(num1))
print(type(num2))
print(type(result))

print('hello world')

x=1
print(x)
print(type(x))
x=100000000000000000000000000000000
print(type(x))

age=input('Please enter your age:')
print(type(age))
print(age)

age1=input('Please enter your age:')
print(type(age1))
print(age1)
age2=input('Please enter your age:')
print(type(age2))
print(age2)
age=age1+age2
print(age)

#Implict Type_casting
age1=int(input('Please enter your age:'))
print(type(age1))
print(age1)
age2=int(input('Please enter your age:'))
print(type(age2))
print(age2)
age=age1+age2
print(type(age))
print(age)

age1=float(input('Please enter age:'))
print(type(age1))
print(age1)
age2=float(input('Please enter age:'))
print(type(age2))
print(age2)
age=age1+age2
print(type(age))
print(age)

#Explict Type_casting
int_value=100
string_value='1.5'
float_value=float(int_value)
print('int value as a flaot:',float_value)
print(type(float_value))
float_value=float(string_value)
print('string value as a flaot:',float_value)
print(type(float_value))

#Complex Number

c1=1
c2=3j
print('c1:',c1,'c2:',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

#Boolean Values

all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))

#If you enter something then it will be true and if you not enter anything then it will be false as output
status=bool(input('ok it is confirmed?: '))
print(status)
print(type(status))

'''
Arithmatic operators are used to perform
some form of mathematical operation
'''

home=10
away=15
print(home+away)
print(type(home+away))
print(10*4)
print(type(10*4))
goals_for= 10
goals_against = 7
print(goals_for-goals_against)
print(type(goals_for-goals_against))

#Flooring values
print(100/20)
print(type(100/20))

#This operator is reffered to as the 
print(100//20)
print(type(100//20))

###################################################
#Day1
#power
a=5
b=6
print(a**b)

#None value
#Python has a special type
#the Nonetype , with a single value, none
winner=None
print(winner is None)
#which we printout as true

winner = None
print('winner:',winner)
print('winner is None :',winner is None)
print('winner is Not None :',winner is not None)
print(type(winner))

#Indentation
num=int(input('Enter value of Num:'))
if num>0:
    print(num)
    
#Else in an If statement
num=int(input('Enter value of Num:'))
if num<0:
    print('It is negative')
else:
    print('It is not negative')    

#The use of elif
saving=float(input('Enter how much saving you have:'))
if saving== 0:
    print("Sorry no savings")
elif saving < 500:
    print("Well Done!")
elif saving<1000:
    print("Thats a tidy sum") 
elif saving<10000:
    print("Welcome sir!")
else:
    print("Thank You!")    
    
#Iteration/Looping
#while loop

count = 1
print('starting')
while(count<=10):
    print(count)
    count+=1
    
#For loop
print('Print out values in a range')
for i in range(2,10):
    print(i)
    #print('Done')
print('Done')   

#Now use an 'anonymous' loop variable
for _ in range(0, 10):
    print('.',end='')
    print()

#Break loop Statement
print('Only print code if all iteration completed')
num = int(input('Enter a number to check for:'))    
for i in range(0,6):
    if i==num:
        break
    print(i,'',end='')
    #print('Done')
print('Done')   

'''
print all odd number from the given list using for loop
  define the start and end limit of the range.
  Iterate from start till the range  in the list using for loop a check if num % 2 = 0.
  It the condition satisfies , then only print the number
'''
start , end =4,19
for num in range (start, end+1):
    if num % 2 !=0:
        print(num,end=" ")
    
#Even number
start , end= 4,20
for num in range(start, end+1):
    if num%2==0:
        print(num,end=" ")
   
start , end= 4,20
step=2
for num in range(start, end+1,step):
    if num%2==0:
        print(num,end=" ")

#Intialize variables
x,y,z=5,6,7
print(x)  
print(y)
print(z)  
x,y,z=5 
print(x)  
print(y)
print(z)   
        
##############################################
#Day3
#Global variables
x="awesome"
def my_function():
    print("python is "+x)
my_function()    

#global and local variables
x="awesome"
def my_function():
    x="fantastic"
    print("python is "+x)
my_function()
print("python is "+x)

#########################
x=range(6)
print(x)
print(type(x))

#########################
#Dictionary 
x={"name":"ram","age":34}
print(type(x))

########################
#assigning values
x=1
y=2.3
z=2+3j
print(type(x))
print(type(y))
print(type(z))

##########################
#Type casting
x=int(1.3)
print(x)
y=float(30)
print(y)

##########################
str1="hello"
str2=2
#str3=str1+str2
#print(str3)
print(f"Hello{str2}")

###########################
#string
#if you want multiple strings
x="""This is python.It is powerful"""
print(x)

###########################
#string slicing
x="""This is python.It is powerful"""
print(x[2:8])

###########################
#slice from the start
print(x[:3])
#x= """I am staying in jay colony"""
#print(x[16:27])
###########################
#slicing to the end
print(x[4:])
###########################
#negative indexing
print(x[-5:-2])

###########################
#modify string
print(x.upper())
################
print(x.lower())

################
#remove white space , removes white space from initial to end
x=" This is python "
print(x.strip())#only remove white space of left hand side
#################
x="This is Python "
print(x.rstrip())#it is going to remove right handside white space
#Replace particular word with another word
x="Hello World"
print(x.replace("Hello","Gello"))

#################################
#use of split which replace white space/or,
x="Hello World"
print(x)
print(x.split(" ")) #separator is space
x="red-green-blue"
print(x.split("-")) #separator is Hypen
x="""This is python.It is simple to understand.Difficult to implement"""
print(x.split("."))

################################
'''Write a python function that accepts a hyphen-separated
sequence of colors as input and return the colors 
in a hyphen-separated sequence after sorting them alphabetically'''

input_string='red-blue-green-yellow'
def sorted_color(input_string):
    string_split=input_string.split("-")
    string_split
    string_sort=sorted(string_split)
    string_sort
    string_join='-'.join(string_sort)
    return string_join
sorted_str=sorted_color(input_string)
print(sorted_str)

###############################################################################
#Day4
#Negative Silicing
x="Python"
print(x[-3])
print(x[-5:5])
print(x[-6:-2])

#Slicing with Negative Indices 
#Sequence[start:stop:step]
#Negative indices can be used  for start and stop.
s="Powerful"
print(s[-6:-2])
print(s[-2:-6])#Output is empty because silicing is in forward direction

#Write program to find string is palindrome or not
def is_palindrome(input):
    if input=="":
        return "INVALIDE INPUT!!!"
    else:
        string=input[::-1]
        if string==input:
            return True
    return False
print(is_palindrome("step on no pets"))    

#find method, Search the string for specified value and returns the location value
x="This is python and it is very powerful"
print(x.find("and"))

########################
#string concateness
x="hello"
y="world"
print(x+y)

########################
#to add white space
print(x+" "+y)

#########################
#string format
x=36
y="my name is Antony"
print(x+y)
#it will give an error

print(f"my name is anthony and my age is {x}")

#########################
quantity=3
item_no=54
price=67
print(f"I want {quantity} pieces and items number is {item_no}, its price is {price}")
my_order="I want {} pieces and item number is {}, Its price is {}"
print(my_order.format(quantity,item_no,price))
##########################
quantity=3
item_no=54
price=67
my_order="I want {0} pieces and item number is {1}, Its price is {2}"
print(my_order.format(quantity,item_no,price))

##########################
#the escape charcter allows you to use double quotes when you normal
text="this is fun fair anb it has got big "round rigo""
#it will show error
text="This is fun fair and it has got big \"round rigo\""
print(text)

#########################
#python boolean
print(10>9)
print(10<9)
print(10==10)

##########################
a=20
b=10
if(a>b):
    print("The a is greater than b")
else:
    print("b is greater than a")  

##########################
#Operator precedence
print(3*3+3/3-3)
"""
Rule for mathematical operations PEMDAS
P:paranthesis
E:exponetial
M:multiplication
D:Division
A:addition
S:Subtraction
"""    
###########################
#identity operators
print(a is b)
print(a is not b)

###########################
#python list
list=["cherry","banana","apple"]
print(list)

########################################################################################
#Day5

#List items are indexed , the first item has index [0], the second item has index [1]
print(list[0])
print(list[1])

#################################
#append() Adds an element at the end of the list
lst=["cherry","banana","apple"]
lst.append("Mango")
print(lst)

#clear removes all the elements from the list
lst=["cherry","banana","apple"]
lst.clear()
print(lst)

###################################
lst=[2,3,4,5,6,7,8]
lst1=[]
for i in lst:
    if i%2==0:
        lst1.append(i)
print(lst1)    

####################################
'''
6 round:
    1.python->even , odd, vowels etc
    2.sql->
    3.Basic concepts of machine learning
    4.Project->assignment
    5.Major Project
    6.HR round
    also apptitude
'''
######################################

#Copy list method
lst=["cherry","banana","apple"]
lst2=lst.copy()
print(lst2)

#####################################
#count() Return the number of times the value "cherry" appears in list
lst=["cherry","cherry","banana","apple"]
lst.count("cherry")

#####################################
#extend() Add the elements of cars to the fruit list:
lst=[1,2,3]
lst1=[4,5,6]
lst.extend(lst1)
print(lst)

######################################
#insert() method , Insert the value "orange" as the second element of the list
lst=["cherry","cherry","banana"]
lst.insert(3,"mango")
print(lst)

#####################################
#pop() Remove the element at the specified position
lst=["cherry","cherry","banana"]
lst.pop(2)
print(lst)

###################################
#remove() Remove the item with the specified value
lst=["cherry","cherry","banana"]
lst.remove("cherry")
print(lst)

##################################
lst=["cherry","cherry","banana"]
lst.reverse()
print(lst)

###################################
#sort() Sort the list alphabetically
lst=["banana","dog","cat","apple"]
lst.sort()
print(lst)

###################################
lst=[40,100,120,200]
lst=sorted(lst,key=int)
print(lst)

#####################################
#Creating a nested list
nested_list=[[1,2,3],["a","b","c"],[True,False]]
print(nested_list)

######################################
#Accessing a specific  element of the last sublist
print(nested_list[0]) #out:'c'

#######################################
#Modifying Element in a nested list
nested_list[1][1]="z"
print(nested_list)

#########################################
#Iterating over a nested list
for sublist in nested_list :
    print(sublist)
    
########################################
#Using Two for loops (Iterate over elements)
for sublist in nested_list:
    for item in sublist:
        print(item,end=" ")

#List Comprehension with Nested lists
#flattening of list
flat_list=[item for sublist in nested_list for item in sublist]
print(flat_list)

######################################
#Adding an Entire sublist
nested_list.append(["new","list"])
print(nested_list)

#######################################
#Adding an Element Inside a Sublist
nested_list[0].append(4)
print(nested_list)

########################################
#Removing an Element from sublist
nested_list[1].remove('b')
print(nested_list)

#############################################
#TUPLE
'''
list is mutable(can modified) but tuple is immutable(can not be modified) 
syntax for list ->[] and syntax for tuple->()
performance of list->slower(due to mutability) and performance of tuple->faster(fixed size and immutability)
Memory Usage list->Use more memory and tuple->Uses less memory
Modification list->can add, remove , or change element and tuple-> cannot remove,add or change any element

'''
###############################################
tup=("cherry","cherry","banana")
print(tup)
print(tup[2])

########################################
#Once Tuple is created , you cannot change its values.Tuple are unchangable
x=("apple","banana","cherry")
print(id(x))
x[1]="kiwi" #error***'tuple' object does not support item assignment

#First convert into list
y=list(x)
print(id(y))
y[1]="kiwi"
#convert list to tuple
x=tuple(y)
print(id(x))
print(x)

#########################################
#tuple can have different datatype
x=("apple",2,"cherry")
print(x)

##########################
#you can access tuple items by referring to the index number, inside 
x=("apple","cherry","banana")
print(x[1])

############################
#to join two or more tuples you can use the + operator
t1=("a","b","c")
t2=(1,2,3)
t3=t1+t2 
print(t3)

############################
#Dictionary
dict1={"Brand":"Maruti","Model":"2345","Year":2011}
print(dict1)
print(len(dict1))
print(type(dict1))

###########################
dict1.get("Model")
dict1.keys()

###########################
car={
     "brand":"Ford",
     "model":"Mustang",
     "year":1964
     }
print(id(car))
x=car.keys()
print(x)

#Adding one more key and value
car["color"]="Black"
print(car)
print(id(car))
x=car.keys()

##############################
#Remove the dictionary element
car={
     "brand":"Ford",
     "model":"Mustang",
     "year":1964
     }
car.pop("model")
print(car)

#######################
#Accessing values in the dictionary
car={
     "brand":"Ford",
     "model":"Mustang",
     "year":1964
     }

for x in car:
    print(car[x])
    
#########################
#Accessing values in the dictionary
#if you want to access both keys and values 
#very important
car={"brand":"Ford","model":"Mustang","Year":1964}
for key,value in car.items():
    print("%s=%s"%(key,value))
for key,value in car.items():
    print(f"{key}:{value}")
    
    
#coping dictionary
car={"brand":"Ford","model":"Mustang","Year":1964}
car2=car.copy()
car2

#coping dictionary using dict
car={"brand":"Ford","model":"Mustang","Year":1964}
car2=dict(car)
car2

#Nested dictionary
our_family={"child1":{"name":"Ram","DOB":"20/10/2005"},"child2":{"name":"Shyam","DOB":"10/10/2005"}}
our_family

#Dictionar methods/functions
#1.clear():Remove all the elements from the car list
car={"brand":"Ford","model":"Mustang","Year":1964}
car.clear()

#fromkey():same value to all keys
x={"key1","key2","key3"}
y=0
d=dict.fromkeys(x,y)
d

#get():To get value of dictionary
car={"brand":"Ford","model":"Mustang","Year":1964}
car.get("model")


#items():Returns key and value pair
car={"brand":"Ford","model":"Mustang","Year":1964}
car.items()

#values():Return values of dictionary
car={"brand":"Ford","model":"Mustang","Year":1964}
car.values()

#sort by keys
d={"b":2,"a":5,"c":1}
d.items()
sort_key=dict(sorted(d.items()))
print(sort_key)

#sort by value
d={"b":2,"a":5,"c":1}
d.items()
sort_value=dict(sorted(d.items(),key=lambda item:item[1]))
print(sort_value)

#assingnment
d={"Apple":80,"Banana":20,"Mango":40,"Grapes":60}

n=int(input("Enter number of item you want to buy:"))
for i in range(0,n):
    f=input("Enter the fruit you want to buy:")


#########################################################################################################################
sorted_dict={'banana':40,'apple':100,'grapes':120,'manago':200}
free_item_key= min(sorted_dict, key=sorted_dict.get)
free_item_value= sorted_dict[free_item_key]
print(f"You will get the lowest priced item'{free_item_key}' ({free_item_value})")
free_item_min=min(sorted_dict,key=sorted_dict.get)
print(free_item_min)

sorted_dict={'banana':40,'apple':100,'grapes':120,'manago':200}
free_item_key= max(sorted_dict, key=sorted_dict.get)
free_item_value= sorted_dict[free_item_key]
print(f"You will get the highest priced item'{free_item_key}' ({free_item_value})")
'''
min(my_dict):Returns the minimum key.
min(my_dict):Returns the minimum value.
min(my_dict, key=my_dict.get):Returns the key corresponding to the minimum values
'''
#########################################################################################################################
#adding values of dictionary 
dict1={'apple':'100', 'grapes':'120','mango':'200','banana':'40'}
sum=0
for value in dict1.values():
    sum=sum+int(value);
print(sum)    

############################################################
#Convert values to  integers and sum them up
dict1={'apple':'100', 'grapes':'120','mango':'200','banana':'40'}
 
total_sum = sum(int(value) for value in dict1.values())
print(total_sum)    

###########################################################
#concatenation of dictionary
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
dict1.update(dict2)
print(dict1)
dict1=dict1|dict2|dict3
print(dict1)

####################################################################
#write a program to check if a given key is already exists
dict1={'a':20,'b':30}
print('a' in dict1)


####################################################################
#write the break statement we can stop the loop if the while 
i=1
while i<6:
    print(i)
    if(i==3):
        break
    i=i+1
    
#suppose you are selling milk 100 liters and there is queue of customers 
#the moment sell reaches to 100 liters, you need to inform to the customer
#that the milk is finished

########################################################################
#Continue to the next iteration if i is 3
i=1
while i<6:
    i=i+1
    if(i==3):
        continue
    print(i)

#Suppose you are standing in queue to auditorium , where students and
#professors are in queue , if the peofessors are there you are allowing
#without checking , but if there is student then he/she is being checked

#############################################################
#for loop
fruits=["Apple","Banana","Cherry"]
for i in fruits:
    print(i)
    
###########################################
#use of brak statement
fruits=["apple","banana","orange"]
for i in fruits:
    print(i)
    if (i=="banana"):
        break
    
#############################################
fruits=["Apple","Banana","Orange"]
for i in fruits:
    if i=="Banana":
        break
    print(i)
    
#############################################
fruits=["apple","banana","cherry"]
for x in fruits:
    if x=="banana":
        continue
    print(x)
    
    #initially it will take x=0
    #which is apple , check s condition
    #print apple
    #second time x=1, checks the
    #condition and continue to the next element
    
################################################
#the range() function

for x in range(6):
    print(x)    
    
#################
for x in range(2,6):
    print(x)
    
################
for x in range(2,30,3):
    print(x)
    
#####################################################
#A nested loop is a loop inside a loop
#the 'inner loop' wiil be executed one time for each iteration 
colors=["green","yellow","red"]
fruits=["guava","banana","apple"]
for x in colors:
    for y in fruits:
        print(x,y)
        

##########################################################
list1=[1,3,4,6,8,-1]
for n in list1:
    if n%2!=0 and n>0:
        print(n," is odd")
##########################################################
#function without any argument
def my_function():
    print("Hello from a function")
    
my_function()

##############################################
#function with argument
def my_function(name):
    print("Hello "+name)
my_function("Pranjali")
        
################################################
#function with positional arguments
def my_function(name1,name2):
    print(name1+" "+name2)
my_function("World","Hello")
#####################################################
#Arbiitrary Arguments, *args
#If you do not know how many argument that
#will be passed into your function
#add a * before the parameter name
#the function definition
def my_function(*args):
    print(args[0]+" "+args[2])
my_function("Pranaji","Vaishnavi","Maithili","xyz")

#######################################################

def myfun(**kwargs):
    for key, value in kwargs.items():
        #print("%s==%s" %(key,value))
        print(f"{key}:{value}")
        
myfun(First_name="papala", mid_name="Mohanlal", last_name="Goyal")        
        
########################################################
#the following example show how to use a default  parameter values

def my_function(country="Norway"):
    print("I am from "+country)
my_function('Dubai')
my_function('India')
my_function() 

#################################################
#Passing a list as a argument
#You can send any data type of argument to a function (string , int , list ect)
Fruits=["orange","Banana","Guava"]
def my_function(Fruits):
    for x in Fruits:
        print(x)
        
my_function(Fruits)

#######################################################
#Return Values
# to let a function returns a value , use yhe return statement:
def my_function(x):
    y=x*5
    return y
my_function(2)

#######################################################
def my_function(x):
    y=x*5
    z=x*7
    return y,z#in the form of tuple
my_function(5)

########################################################
#pass function
def my_function1():
    pass

#Recursive function
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
factorial(3)
factorial(6)

#A lambda function is a small
#anonymous function
#A lambda function can take any number of arguments
#but can have only one expression
def add(a):
    sum=a+10
    return sum
add(20)

add=lambda a:a+10
print(add(20))

mul=lambda a:a*20
print(mul(10))

########
#lambda function can take any number of arguments:
add= lambda a,b:a+b
print(add(5,7))

#finding odd numbers from the list
lst=[34,12,64,55,75,13,63]
odd_lst=list(filter(lambda x:(x%2 !=0),lst))
print(odd_lst)

#even
lst=[2,8,0,45,34]
even_lst=list(filter(lambda x:(x%2==0),lst))
print(even_lst)


####################################
######
#map (function,iterable)
sqr=list(map(lambda x:(x**2),1))
print(sqr)

###############################################
text="apple,banana,orange"
words=text.split(",")#split by comma
print(words)#output is:['apple', 'banana', 'orange']

#############################################
new_text="-".join(words) #join with '-'
print(new_text)#output is:apple-banana-orange

######################################################
#find() & index()-Find Substriing
#find() returns the index of the first occurence
#index() same but it raise error if it not found
text="Hello XYZ"
print(text.find("XYZ"))
print(text.find("Python"))#output:-1
print(text.index("Hello"))
print(text.index("Python"))#Output:ValueError: substring not found

########################################
#count()-Count substring Occurence
text="Hello Hello Python"
print(text.count("Hello"))

########################################
#startswith() & endswith() -Check Start/End
text="Python is great"
print(text.startswith("Python"))#Output:True
print(text.endswith("great"))#Output:True

########################################
#isalpha(),isdigit(), isalnum()
#isalpha()->Return true if all characters are letter
#isdigit()->Return true if all characters are digit
#isalnum()->Return true if all characters are letters as well as digit(either letters or numbers)
text="Maithili1234"
print(text.isalpha())
print(text.isdigit())
print(text.isalnum())#true

t="1"
print(t.isdigit())
##########################################
#isupper()->Checks if all characters are in Uppercase
#islower()->Check if all characters are in Lowercase
t="HELLO"
t2="HELLO123"
t3="1234"
count=0
for i in range(len(t)):
    if t[i].isupper():
        count+=1
print(count)#output:5

for i in range(len(t2)):
    if t2[i].islower():
        count+=1
print(count)#output:0

for i in range(len(t3)):
    if t3[i].isupper():
        count+=1
print(count)#output:0

#Does it end with fullstop?
str="There are no traffic jams along the extra mile."
ans=str.endswith(".")
print(ans)

#####################################################
#Check in list there is any duplicate or not
lst1=[6,8,5,6,7]
lst1.sort()
print(lst1)
def is_duplicate(lst1):
    for i in range (len(lst1)-1):
        #compare current number with next number present in list
        if (lst1[i]==lst1[i+1]):
            return True
    return False
print(is_duplicate(lst1))    
######################################################
'''
Alex wants to buy exactly N bananas fron two vendors.
Each vendor sells bananas in fixed-sized bunches.
Alex can only purchase full bunches and not individual bananas.
He needs your help to determine the minimum cost required to buy exactly N bananas.

'''
##############################
no_bananas=int (input("Enter no of bananas to be purchased: "))
lot1=int(input("What is a size of lot1 that vendor1 provides: "))
price1=int(input("What is a price of lot1: "))
lot2=int(input("What is a size of lot2 that vendor2 provides: "))
price2=int(input("What is a price of lot2: "))

def min_cost(no_bananas, lot1,price1,lot2,price2):
    lot_a=no_bananas/lot1
    print(f'lot_a:{lot_a}')
    
    lot_b=no_bananas/lot2
    print(f'lot_b:{lot_b}')
    cost_a=lot_a*price1
    print(f'cost_a:{cost_a}')
    cost_b=lot_b*price2
    print(f'cost_b:{cost_b}')
    return min(cost_a,cost_b)
min_cost(no_bananas,lot1,price1,lot2,price2)

#################################################
'''
Steps of bubble sort
start from the first element and compare it with the next ele
if the first element is greater than the next ,swap them
move to the next pair and repeat 
'''
def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j] 
    return lst
lst = [5,3,8,4,2]
bubble_sort(lst)

#################################################################
def gcd(a,b):
    while b:
        a,b = b,a%b # replace a with b and b with remainder
    return a
#input
num1 = int(input("Enter first number:"))
num2 = int (input("Enter second number:"))
#output
ans = gcd(num1,num2)
print(f"GCD of (num1) and (num 2) is:{ans}")


#################################################################
import math

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
ans=math.gcd(num1,num2)

print(f"GCD of {num1} and {num2} is:{ans}")

##################################################################
#Find Second Largest Element in an array
def second_largest(lst):
    unique_nums=list(set(lst))
    #The list is first converted to a set (set(lst)) to 
    unique_nums.sort(reverse=True)
    #It is then converted back into a list (unique_nums)
    #the sort(reverse=true) method in python sort
    # a list in descending order(from highest to lowest)
    if len(unique_nums)>1:
        return unique_nums[1]
      '''however if the list contains only one unique number
        (e.g [99,99,99] becomes [99] after removing duplicates),
        there is no second largest element
        
        If unique nums has only one element,
        trying to access unique nums[1]
        To prevent this, len(unique_nums)> 1 is checked,
        if unique_nums has only one element , the function 
       '''
    else:
        return None
lst=[7,8,3,5,1,2,2]
print("second largest element from the array is: ",second_largest(lst))
###################################################################
def bubble_sort(lst):
    n = len(lst)
    for i in range(n-1):
        
        for j in range(n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j] 
    return lst
lst = [5,3,8,4,2]
bubble_sort(lst)
print(lst[-2])#second largest element
print(lst[1])#second smallest element
 
################################################################
#find second smallest number
def second_smallest(lst):
    unique_nums=list(set(lst))
    unique_nums.sort(reverse=False)
    
    if len(unique_nums)>1:
        return unique_nums[1]
    else:
        return None
lst=[5,3,8,4,2]
print("second smallest number:",second_smallest(lst))        

###################################################################
'''
To identify missing numbers 
the sum of the first n natural numbers is given by:
    s=1+2+3+4+......+n
    expected_sum=n*(n+1)//2
    Example Calculations:
        Lets calculate the sum of the first 5 natural:
        1+2+3+4+5=15
        using expected_sum=n*(n+1)//2=5*6//2=15
        
'''
def missing_num(lst,n):
    expected_num=n*(n+1)//2
    actual_num=sum(lst)
    missing_num=expected_num-actual_num
    return missing_num
lst=[1,2,4,5,6]
n=6
print("Missing number: ",missing_num(lst,n))
##########################################################
#Reverse a string without built-in function

def rev_string(s):
    rev_s=s[::-1]
    return rev_s
s="My name is anthony"
rev_s=rev_string(s)
print(rev_s)
########
rev_string=input("Enter a string: ")[::-1]
print(rev_string)
############################################################
#find LCM of Two Numbers
num1=int(input('Enter first  number: '))
num2=int(input('Enter second number'))

def gcd(num1,num2):
    while num2!=0:
        num1,num2=num2,num1%num2
    return num1

gcd(num1,num2)
def lcm(num1,num2):
    lcm=abs(num1*num2)/gcd(num1,num2)
    return lcm
lcm(num1,num2)    

#############################################################
'''
Gary is an avid hiker. He tracks his hikes meticulously,
 paying close attention to small details like topography.
 During his last hike, he took exactly n steps. 
 For every step he took, he noted if it was an uphill (U) 
 or a downhill (D) step. Gary’s hikes start and end 
 at sea level.

We define the following terms:

A mountain is a non-empty sequence of consecutive
 steps above sea level, starting with a step up 
 from sea level and ending with a step down to sea level.
 A valley is a non-empty sequence of consecutive
 steps below sea level, starting with a step down 
 from sea level and ending with a step up to sea level.
Given Gary’s sequence of up and down steps 
during his last hike, find and print the number of valleys
 he walked through.

Gary is hiking, and he records each step as either U (uphill) or D (downhill). He always starts and ends at sea level (0 altitude).

We need to count the number of valleys he walks through.

What is a valley?
A valley is when:

Gary goes below sea level (altitude becomes negative).
He then comes back to sea level.
Example Walkthrough
Let’s say Gary takes the following 8 steps:
"DDUUUUDD"
 
'''
#count the valleys:
def count_valleys(n,paths):
    elevation=0 # Starting at sea level
    valley_count=0 #Counter for valleys
    
    for step in paths:
        if step =='U':# going up
           elevation+=1 
           if elevation==0: #IF we just came back 
                            # to sea level , a valley ended
              valley_count+=1 #Why check if elevation == 0?
              #inside if step == 'U' ?
              #A valley is only completed when coming up(U)
              #back to sea level (0).
        else:
            step=='D' #Going down
            elevation-=1 
               
    return valley_count 

# Example Usage
n=8
path="UDDDUDUU"
print("Total Valleys", count_valleys(n,path))  


############################################################
#Left rotation
'''
Problem Statement

A left rotation operation on an array shifts
each of the array's elements unit to the left.
For example , if 2 left rotation 
'''

def left_rotate(lst,d):
    #find the length
    n=len(lst)
    d=d%n
    left_rot=lst[d:]+lst[:d]
    return left_rot
lst=[1,2,3,4,5]
d=2
result=left_rotate(lst,d)
print(*result)    

###########################
def right_rotate(lst,d):
    #find the length
    n=len(lst)
    d=d%n
    right_rot=lst[:d]+lst[d:]
    return right_rot
lst=[1,2,3,4,5]
d=2
result=right_rotate(lst,d)
print(*result)    

######################################################
#Create matrix and print matrix
mat1=[[1,2,3],
      [4,5,6],
      [7,8,9]
      ]
rows=len(mat1)
columns= len(mat1[0])

print("Rows: ",rows)
print("Columns: ",columns)

for i in range(rows):
    for j in range(columns):
        print(f"Element at [{i}][{j}]={mat1[i][j]}")
########################################################
#matrix addition
mat1=[
      [1,2,3],
      [4,5,6],
      [7,8,9]
      ]
mat2=[
      [1,2,3],
      [4,5,6],
      [7,8,9]
      ]
result=[
      [0,0,0],
      [0,0,0],
      [0,0,0]
      ]

rows=len(mat1)
cols=len(mat1[0])

for i in range(rows):
    for j in range(cols):
        result[i][j]=mat1[i][j]+mat2[i][j]
result

#################################################################
#print the digonal of matrix
mat1=[[1,2,3],[4,5,6],[7,8,9]]
rows=len(mat1)
cols=len(mat1[0])
for i in range(rows):
    for j in range(cols):
        if i==j:
            print(mat1[i][j])
        
####################################################################
#Check if the matrix is sparse
#A sparse matrix is a matrix in which most
#of the elements are zero . If the number of
#zero element is greater is greater than half of the total elements
#mat1=[[1,2,0],[0,4,0],[0,0,6]]
mat1=[[1,2,3],[5,4,0],[7,0,6]]
rows=len(mat1)
cols=len(mat1[0])
count=0
for i in range(rows):
    for j in range(cols):
        if mat1[i][j]==0:
            count+=1 
if count>(rows*cols)/2:
    print('Sparse')
else:
    print('not sparse')    

#############################################################################
#Program to check if two matrices are identical
#rows must be equal to columns
#contents must be equals to both matrix
def are_identical(mat1,mat2):
    #Compare dimension inside the function
    rows1,cols1=len(mat1),len(mat1[0])     
    rows2,cols2=len(mat2),len(mat2[0])
    
    #Check if the dimensions are same
    if rows1 != rows2 or cols1 != cols2:
        return False #Matrix , must have same size
    
    #Compare elements
    for i in range(rows1): #Iterate over rows
        for j in range(cols1): #Iterate over columns
            if mat1[i][j]!=mat2[i][j]:
                return False #If any element differs
    return True

#Example
mat1=[[1,2,3],[4,5,6]]
mat2=[[1,2,3],[4,5,6]]    

#Function call
print("All the matrices identicals?",are_identical(mat1,mat2)) 

#Example2
mat1=[[1,2,3],[4,5,6]]
mat2=[[1,2],[3,4]]   
print("All the matrices identicals?",are_identical(mat1,mat2)) 

###################################################################################
'''
Given 2D array convert into 1D array in Spiral Order
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16

'''

#############################################################
#Write a program to remove item from set
st={1,4,6}
st.remove(4)
print(st)

#Write a program to find intersection of sets
st1={1,4,6}
st2={2,4,6}
#intersection
st=st1&st2
print(st)

#Union of sets
st=st1|st2
print(st)

dict={x:x**2 for x in range(1,16)}
print(dict)

##################################################################
#Write a program to find maximum and minimum of sets
m_set=max(st)
print(m_set)
mi_set=min(st)
print(mi_set)

###################################################################
#Given  a string , return string made of two character
#where n is length of string if the input is wipro
#wiwiwiwiwi
t1="wipro"
t2=t1[:2]
final=t2*len(t1)
print(final)

#Given a string , if first and last character is x, then 
#the string without x , else display as it is
text='madam'
text='madan'
if(text[0]==text[-1]):
    final=text[1:-1]
    print(final)
else:
    print(text) 
    
###########################
#Given string and an integer n,
#return a string made of n repetition
#of the last n character of string 
#You may assume that n is between 0 and the length
#of the string (inclusive)

#for example, if the input are "Wipro" and 3,
#then the output should be "propropro".
text="wipro"
n=3
text1=text[2:5]
final=text1*n
print(final)

#########################################################
#you are signing in bank and bank has forwarded OTP
#take the OTP and check whether it is numeric and 6 digits only
#if valid print ok else  print non valide
    


########################################################################
###SETS DATA STRUCTURE
#remove element
s={1,4,6}
s.remove(4)
print(s)
#find intersection of sets
s1={1,4,0,6}
s2={2,4,6,0}
s=s1&s2
print(s)
#union of sets
s1={1,4,0,6}
s2={2,4,6,0}
s=s1|s2
print(s)

#printing dictionary
#dictionary comprehension
d={x:x*x for x in range(1,16)}
print(d)

#to find minimum and maximum value of set
max_set=max(s)
print(max_set)
min_set=min(s)
print(min_set)

###############
#string data structure
#printing first two char n number of times
#n=length of string
text='wipro'
t1=text[:2]
final=t1*len(text)
print(final)

'''if first and last char is x 
then display the string without x,else
display as it is'''
t='madam'
if (t[0]== t[-1]):
    f=t[1:-1]
    print(f)
else:
    print(t)
    
############################
'''given a string and integer n
return strinng made of n repitatons
of the last n characters of the string
you may assume that n is between 0 and length
of string (exclusive)'''
t='wipro'
n=3
t1=t[2:5]
final=t1*n
print(final)

'''you are signing in bank and bank has 
forwarded OTP and check wheather it is
numeric and 6 digits .if valid print ok
else print non valid'''
otp=input("Enter otp forwarded")
if otp.isdigit() and len(otp)==6:
    print("ok")
else:
    print("invalid OTP")
    
#########exception handling
#zero division error
a=10
b=0
try:
    res=a/b
except ZeroDivisionError:
    print("cannot divide by 0!")

#index error
num=[1,2,3]
#print(num[5])
try:
    print(num[5])
except IndexError:
    print("index out of range error")

#handling exceptions withoout naming them
try:
    n=50
    d=int(input('enter denominator'))
    quotient=(n/d)
    print("divison performed succesfully")
except ValueError:
    print("only integere should be entered")
except:
    print("oops...some exception raised")

#handling exception using using try..except..else
try:
    n=50
    d=int(input('enter denominator'))
    quotient=(n/d)
    print("divison performed succesfully")
except ZeroDivisionError:
    print("division by zero not allowed")
except ValueError:
    print("only integere should be entered")
else:
    print("division is",quotient)

#xception handling using try except else finally
try:
    n=50
    d=int(input('enter denominator'))
    quotient=(n/d)
    print("divison performed succesfully")
except ZeroDivisionError:
    print("division by zero not allowed")
except ValueError:
    print("only integere should be entered")
else:
    print("division is",quotient)
finally:
    print("over and out")
    
#filenot found
with open('C:/Users/Lenovo/Desktop/pythonfundamentals/py_digits.txt','r') as file:
    contents=file.read()
print(contents.rstrip())
 

try:
    with open('C:/Users/Lenovo/Desktop/pythonfundamentals/py_digits.txt','r') as file:
        contents=file.read()
except FileNotFoundError:
    print("file not found")

#permision error
with open('C:/Users/Lenovo/Desktop/pythonfundamentals/py_digits.txt') as file:
    contents=file.read()
print(contents.rstrip())
#with try and catch
try:
    with open('C:/Users/Lenovo/Desktop/pythonfundamentals/py_digits.txt') as file:
        contents=file.read()
    print(contents.rstrip())
except PermissionError:
    print("dont have permisiion to access file ")
    
    
#attribute error
obj=None
print(obj.some_attribute)
if obj is not None:
    print(obj.some_attribute)
else:
    print("object is none!")
    
#MemoryError
l=[1](10*10)  #raises memory error

#handling using generator
def generate_num():
    for i in range(10**10):
        yield i #yield numbers one by one  prevent memory error
gen=generate_num()
print(next(gen))
#####################################
import sys
sys.setrecursionlimit(1000) #Set recursion limit to a

def safe_recursive_function(depth=0, max_depth=10):
    if depth >= max_depth:
        return "Done"
    return safe_recursive_function(depth + 1, max_depth)

print(safe_recursive_function()) #Works safety
#################################################################

#Write a program to read the entire content from a txt file
with open(r"E:\1-Python\pi_digits.txt",'r') as File:
    contents=File.read()
    print(contents.rstrip())

#Write a program to  read first n lines from a txt file.
with open(r"E:\1-Python\pi_digits.txt",'r') as File:
    lines=File.readlines()
    if lines:
        print("First line: ",lines[0].strip())
        print("last line:",lines[-1].strip())

#########################################################
#Write a program to accept input from user and append it
filename="E:/1-Python/pi_digits.txt"
with open(filename,'w') as file:
    file.write("I love programming.\n")
    file.write("I love creating nem games.\n")
    in_line=input("Enter the line: ")
    file.write(in_line)
    
###########################################################
#Write a program to read contents from a txt file line by
#line and store each line into a list
filename="E:/1-Python/pi_digits.txt"
with open(filename,'r') as file:
    lines=file.readlines()
    pi_string=[]
    for line in lines:
        pi_string.append(line.rstrip())
       #pi_string += line.rstrip()
        print(pi_string)
    print(len(pi_string))    
############################################################
#Write a program to find the longest word from the txt file
#contents, assuming that the file will have only one longest
filename="E:/1-Python/pi_digits.txt"
with open(filename,'r') as file:
    lines=file.readlines();
    longest_word=''
    for line in lines:
        words=line.split()
        for word in words:
            if(len(word)>len(longest_word)):
                longest_word=word
print("The longest word: ",longest_word)                
###################
#smallest word:
filename="E:/1-Python/pi_digits.txt"
with open(filename,'r') as file:
    lines=file.readlines();
    smallest_word=None
    for line in lines:
        words=line.split(' ')
        for word in words:
            if(smallest_word==None or len(word)<len(smallest_word)):
                smallest_word=word
print("The smallest word: ",smallest_word)  

#########################################################################
#Write a program to count the frequency of a
#user -entered word in a txt file.

filename="E:/1-Python/pi_digits.txt"  
input_line=input("Enter the text:")
words=input_line.split()
word_count=len(words)

#write user input to the file
with open(filename,'w')as file:
    file.write(input_line)
#display the word count
print("The total words entered:",word_count)   

###############################################################
'''
Write a program to accept two numbers from the user and perform division. If any exception occurs
print an error message or else print the result
''' 
try:
    num1=float(input("Enter number1: "))
    num2=float(input("Enter number2: "))
    num=num1/num2
    print("The result is: ",num)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter numeric values only.")
    num1=float(input("")) 
    
#####################################################################
'''
Write a program to accept number from user and check it is prime or not
.If user enters anything other than number, handle the exception and print
an error message
'''

def is_prime(num):
    if num< 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

try:
   num = int(input("Please enter the number: "))
   if is_prime(num):
       print("Entered number is prime number")
   else:
       print("Entered number is not an prime number")
except ValueError:
   print("Please Enter a valid integer!!!")   
   
'''
Write a program to accept the file name
to be opened from the user,
if file exist print the contents of the file
in title case or else handle the exception and 
print an error message.
'''   
try:
    file_name=input("Please enter file name with absolute path: ")
    with open(file_name,'r') as file:
        content = file.read();
        print(content.title())
except FileNotFoundError:
    print("Error: File not found.")       
except PermissionError:
    print("Error: You don't have permission to access file") 
    
'''
Declare a list with 10 integer and ask the user to enter an index 
check whether the number in that index is positive or negative 
number . If any invalid index is entered handle the exception and print an error message
'''
numbers = [5, -3, 7, -1, 12, -8, 9, -6, 15, 2]

try:
   index= int(input("Enter an index (0-9): "))
   value = numbers[index]
   if value > 0:
      print(f"The number at index {index} is positive.")
   else:
      print(f"The number at index {index} is negative.") 

except IndexError:
   print("Error: Index out of range. Please Enter valid index") 
except ValueError:
   print("Error:Please enter valid integer")           


