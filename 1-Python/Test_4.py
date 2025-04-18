# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 08:23:54 2025

@author: maith
"""

'''
Write a Python function named collect_employee_details() that collects details of a
specified number of employees. The function should:
1. Prompt the user to enter the number of employees (residents).
2. For each employee, collect:
o Name
o Age
o Designation
o Band (should be one of 'A', 'B', 'C', or 'D'; case-insensitive input but stored in
uppercase)
3. Validate the following:
o Number of residents must be greater than 0.
o Age must be between 21 and 58 (both inclusive).
o Band must be one of 'A', 'B', 'C', or 'D'.
If any validation fails, print "Invalid" and terminate the function immediately.
Test Case
No. Input Expected Output
TC1 Number of residents: 0 Invalid
TC2 Number of residents: -2 Invalid
TC3 Number of residents: 1, Age: 20 Invalid
TC4 Number of residents: 1, Age: 59 Invalid
TC5 Number of residents: 1, Band: E Invalid
TC6 Number of residents: 1, Age: 30, Band: b (Valid input, continue)
TC7 Number of residents: 2, First entry valid, Second
entry Age: 60
Invalid
TC8 Number of residents: 2, First entry valid, Second
Band: F
Invalid
TC9 Number of residents: 2, All inputs valid (Name,
Age, Designation, Band)
Function completes without
printing Invalid
Write a Python function longest_negative_sum(input1, input2) that takes two 
'''
 
########################################
def collect__employee_details(n):
    if n<=0:
        print("Invalid")
        return
    
    for i in range(n):
        name = input("Enter name of employe: ")
        
        age = int(input("Enter age of Employee: "))
        
        if age < 21 or age > 58:
            print("Invalid")
            return
        
        designation = input("Enter the designation: ")
        
        band = input("Choice band in this (A,B,C,D):")
        
        if band not in ['A','B','C','D','a','b','c','d']:
            print("Invalid")
            return
    print("Successfully done!!")    
        
num = int(input("Enter Number of residents: "))
collect__employee_details(num)

#################################################        
'''
Write a Python function longest_negative_sum(input1, input2) that takes two
parameters:
 input1: A list of integers.
 input2: (length of list)
Your task is to identify all contiguous negative number sequences in the list input1, and:
1. Find the longest such sequence(s) (i.e., the ones with the most consecutive negative
numbers).
2. If multiple sequences share the same maximum length, include all of them.
3. Calculate and return the sum of the individual sums of these longest sequences.
4. If there are no negative numbers, return -1
Test Case No. Input1 Expected                  Output Explanation
TC1           [1, 2, 3, 4]                      -1 No negative numbers
TC2           [-1, -2, -3,4, -1, -2]            -6 Two negative sequences of equal max length 3: [-1, -2, -3] = -6 and [-1, -2] = -3 → Only first has max length = 3, sum = -6
TC3           [4, -1, -2, -3, -4, 5]            -10 One sequence of length 4: [-1, -2, -3, -4]
TC4           [4, -1, -2, 0,-3, -4]             -10 Two sequences of length 2 → [-1, -2] and [-3,-4], sum = -3 + -7 = -10
TC5           [-5]                              -5 Single negative element
TC6           [-1, -2, 0, -1, -2, 0, -1,-2]     -9 Three sequences of equal length 2 → sums: -3, -3, - 3 → Total = -9
TC7           []                                -1 Empty list
TC8           [-1, -2, -3, -4, -5]             -15 One long negative sequence
TC9           [1, -1, -2, 3,-3, -4, 5, -5,-6]  -21 Three sequences of equal max length 2 → [-1, -2], [-3, -4], [-5, -6] → Sum = -3 -7 -11 = -21
''' 
######################################
lst=[1, 2, 3, 4]
lst=[-1, -2, -3,4, -1, -2] 
lst=[4, -1, -2, -3, -4, 5]
lst=[4, -1, -2, 0,-3, -4]
lst=[-5]
lst=[-1, -2, 0, -1, -2, 0, -1,-2]
lst=[]
lst=[-1, -2, -3, -4, -5]
lst=[1, -1, -2, 3,-3, -4, 5, -5,-6]
curr_len=0
curr_sum=0
max_len=0
longest_sums=0
for num in lst :
    if num<0 :
        curr_len+=1
        curr_sum+=num
    else :
        if curr_len >0 :
            if curr_len>max_len :
                max_len=curr_len
                longest_sums=[curr_sum]
            elif curr_len==max_len :
                longest_sums.append(curr_sum)
            curr_len=0
            curr_sum=0
if curr_len>0:
    if curr_len>max_len :
        max_len=curr_len
        longest_sums=[curr_sum]
    elif curr_len==max_len :
        longest_sums.append(curr_sum)
print(sum(longest_sums)if longest_sums else -1)











