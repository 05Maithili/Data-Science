# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 08:15:24 2025

@author: maith
"""
#pre- requisite to decorators

def plus_one(number):
    number1 = number + 1 
    return number1
plus_one(5) #output : 6

#############################################
#Defining Functions Inside other function

def plus_one(number):
    
    def add_one(number):
        number1=number + 1
        return number1
    
    result = add_one(number)
    return result

plus_one(5)
#############################################
#Passing function as Argument
#to other function

def plus_one(number):
    result1 = number + 1
    return result1

def function_call(function):
    result = function(5)
    return result

function_call(plus_one)

##############################################
#Function Returning other function

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi 
#hello_function()
hello = hello_function()
hello()
#Always remember when you call hello_function()
#directly then it will display object not hi
#therefore you need to assign it to hello first
#then call hello() function

###############################################
#Need for decorators
import time
def calc_square(num):
    start=time.time()
    result=[]
    for i in num:
        result.append(i*i)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time for execution square is {total_time}")
    return result

def calc_cube(num):
    start=time.time()
    result=[]
    for i in num:
        result.append(i*i*i)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time for executin of cube is {total_time}")
    return result
array=range(1,100000)
out_sqaure=calc_square(array)
out_cube=calc_cube(array) 
#########################################
#that takes in a function and
#return it by adding some functionality
def say_hi():
    return 'Hello There'

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper 

decorate = uppercase_decorator(say_hi)
decorate()

###########################################
# However Python provides a much easier way
# for us to apply decorators.
# We simply use the @ symbol before
# the function we'd like to decorate
###########################################
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper 

@uppercase_decorator
def say_hi():
    return 'Hello There'
say_hi()

###########################################
# Applying Multiple Decorators
# that we've called them

def split_string(function):
    def wrapper():
        func = function()
        spliting_string = func.split()
        return spliting_string 
    return wrapper

def uppercase(function):
    def wrapper():
        func = function()
        uppercase_str= func.upper()
        return uppercase_str
    return wrapper

@split_string 
@uppercase
@uppercase
def say_hi():
    return 'Hello There'
say_hi()

##############################################################
import time
def time_it(func):
    #this is a decorator function that takes another function as argument
    
    def wrapper(*args, **kwargs):
        #*args and **kwargs allow wrapper
        #to accept any number of positional and keyword
        start = time.time()
        result = func(*args, **kwargs)
        
        #Calls the orignal function (func)
        #with the provided arguments
        
        end = time.time()
        print(func.__name__+"took"+str((end-start)*1000) + "mil sec")
        return result
    return wrapper

@time_it 
def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number*number)
    return result

@time_it 
def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number*number*number)
    return result

array = range(1,100000)

out_square = calc_square(array)
out_cube = calc_cube(array)  

##############################################################
#Automarically logs function calls and their arguements
 
def log_decorator(func):
    def wrapper(args,*kwargs):
        print(f"calling{func.name}with{args}{kwargs}")
    return wrapper 
@log_decorator
def add(a,b):
    return a+b
print(add(3,4))
###############################################################
#Access Control / Authentication
#Check if a user is authentication before executing
# a function 
def auth_required(func):
    def wrapper(user):
        if not user.get("authenticated", False):
            #the .get("authenticated",False) method
            #is used to safety retrieve the value of
            #the "authenticated" key from the
            #dictionary.
            print("Access Denied")
            return
        return func(user) 
    return wrapper 

@auth_required
def dashboard(user):
    print(f"Welcome {user['name']}!")
user1 = {"name": "Alice", "authenticated": True}
user2 = {"name": "Bob", "authenticated": False}
dashboard(user1)  # Expected: "Welcome Alice!"
dashboard(user2)  # Expected: "Access Denied"

#############################################################################
#Input  validation
#Ensures input meet certain criteria before executing
def validate_positive(func):
    def wrapper(x):
        if x < 0:
            raise ValueError("Negative value not allowed")
        return func(x)
    return wrapper 

@validate_positive 
def square_root(x):
    return x**0.5
    
print(square_root(4)) # Works fine
print(square_root(-4)) #Error ValueError: Negative value not allowed

############################################################################
import time

def rate_limiter(max_calls,time_frame):
    calls = []
    
    def decorator(func):
        def wrapper(*args , **kwargs):
            now = time.time()
            while calls and now - calls[0] >time_frame:
                calls.pop(0)
                
            if len(calls) >= max_calls:
                print("Rate limit exceeded. Try again later!!")
                return
            
            calls.append(now)
            return func(*args,**kwargs)
        return wrapper 
    return decorator

'''
Condition: while calls and now - calls[0] > time_frame

calls is a list that stores timestamps of
previous function calls

calls[0] represents the oldest function call
in the list.

now is the current time when the function
is being called

now - calls[0] computes how long ago the oldest 
call occured.

If that time exceed it 
'''

@rate_limiter(3,10) #Max 3 in 10 second

def say_hii():
    print("Hello")
    
say_hii()
say_hii()
say_hii()
say_hii()   #this call will be rate-limited 
##########################################################################
lst = []
for num in range(0,20):
    lst.append(num)
print(lst)
#########################################
#we can write  same method using list comprehension
lst = [num for num in range(0,20)]
print(lst)

##################################
names =["dada","kaka","mama",]
lst = [name.capitalize() for name in names]
print(lst)
########################
def is_even(num):
    return num%2==0
lst = [num for num in range(10) if is_even(num)]
print(lst)
######################################
lst = [f"{x}{y}"for x in range(3) for y in range(3)]
print(lst)
#########################################

###############################################
# Generator
# It is another way of creating iterators
# In  a simple way where
# It uses the keyword "Yeild"
# Instead of returning it in a defined  function
# Generators are implemented using a function
gen = (x for x in range(3))
print(gen)
for num in gen:
    print(num)
################# 
gen = (x
       for x in range(3)
       )
next(gen)   

############################
gen = (x for x in range(3))
next(gen)
next(gen)

############################
# Function which returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)

##################################
# now instead of using for loop we can write our own gene
gen = range_even(6)
next(gen)
next(gen)

##########################################
# let us hide password entered on screen
# Chaining Generators
def length(itr):
    for ele in itr:
        yield len(ele)
        
def hide(itr):
    for ele in itr:
        yield ele*'*'

'''
"ele" appears to be a placeholder for an element
from an iterable. The astrisk (*) is likely
just a character used to represent a placeholder
or a wildcard.
For instance, if you're iterating 
over a list of elements , "ele"
could symbolize any element in that list.
It's a generic representation 
that doesnt  correspond to any specific syntax 
in python or iteratools.
'''

passwords = ["not-good", "give'm-pass", "00100=100"]

for password in hide(length(passwords)):
    print(password)
    
##############################################################
#Enumerate
#printing list with index
lst = ["milk", "Egg" ,"Bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')
############
# same code can be implemented using enumerate
lst = ["milk","Egg","Bread"]
for index, item in enumerate(lst,start = 1):
    print(f"{index} {item}")

#########################
# Use of zip function
name = ['dada', 'mama', 'kaka'] 
info = [9850, 6032, 9785]
for nm,inf in zip(name,info):
    print(nm,inf)
    
####################################
# Use of zip function with mis match list
name = ['dada', 'mama','kaka','baba']
info = [9850,6032,9785]
for nm,inf in zip(name,info):
    print(nm,inf)    
# It will not display excess mismatch item in name for example baba
####################################
##zip_longest
from itertools import zip_longest
name = ['baba', 'kaka', 'mama','dada']
info = [9850, 6032,9768]
for nm,inf in zip_longest(name,info):
    print(nm,inf)  
    
###################################
#use of fill value instead None
from itertools import zip_longest
name = ['dada','mama','kaka','baba']
info = [9850, 6032, 3297]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf)    
    
######################################
# use of all(), if all the values are
# true then it will produce output
lst = [2,3,-6,8,9] #values must be non zero, +ve, -ve
if all(lst):
    print("all values are true")
else:
    print("There are null values")
    
##########################
lst=[2,3,0,8,9]
if all(lst):
   print("all values are true")
else:
   print("There are null values")    
   
##########################################
 
lst = [0,0,0,0,0]
if any(lst):
    print("It has some non zero value")
else:
    print("All values are null in list")  
    
#######################################
#use of any if any one  non zero value

lst = [0,0,0,-8,0]
if any(lst):
    print("It has some non zero value")
else:
    print("Useless")    
    
#########################################
#count()
from itertools import count
counter = count()
print(next(counter)) 
print(next(counter)) 
print(next(counter)) 
   
###########################################
# Now let us start from 1
from itertools import count
counter = count(start =1)
print(next(counter))
print(next(counter))    
print(next(counter))    

############################################
#cycle()
#suppose you have repeated tasks to be done, then you can
import itertools

instructions = ("Eat","code","sleep")
for instruction in itertools.cycle(instructions):
    print(instruction)
#############################################
# Define the number of patients and consultation time
n = int(input("Enter the total number of patients visiting the hospital daily: "))
t = int(input("Enter the consultation time per patient in minutes: "))

# Find the time for the 50th patient to meet the doctor
if n < 50:
    print("The 50th patient won't be treated today as only", n, "patients visit daily.")
else:
    # Calculate the time for the 50th patient in minutes
    time_for_50th_patient = 50 * t

    # Convert minutes to hours and minutes format
    hours = time_for_50th_patient // 60
    minutes = time_for_50th_patient % 60

    print(f"The 50th patient will meet the doctor after {time_for_50th_patient} minutes.")
    print(f"This is equivalent to {hours} hours and {minutes} minutes.")
    
    
    
    
    