#Mario pyramids
for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()#newline
    '''
    #SQUARE
    Output:
    * * * * 
    * * * * 
    * * * * 
    * * * * 
    ''' 
##########################
for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()    
    '''
    #PYRAMID
    Output:
    * 
    * * 
    * * * 
    * * * *
    ''' 
#########################
for i in range(4):
    for j in range(4-i):
        print("*",end=" ")
    print()   
    '''
    #INVERTED PYRAMID
    Output:
    * * * * 
    * * * 
    * * 
    * 
    ''' 
#########################
for i in range(4):
    for j in range(4):
        print("*",end=" ")
        print()
    '''
    #
    Output:
    * 
    * 
    * 
    * 
    * 
    * 
    * 
    * 
    * 
    * 
    * 
    * 
    * 
    * 
    * 
    * 
    ''' 

#############################################
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

#############################################
str='Elbow'
str.replace('',' ').lower()
a=list(str.replace(""," ").lower())
sorted(a)

#############################################
#anagram->two different words have all characters some 
def are_anagram(str1,str2):
    #convert the str1 and str2 in to list regard
    a=list(str1.replace(""," ").lower())
    b=list(str2.replace(""," ").lower())
    
    if(len(a)!=len(b)):
        return False
    else:
        return(sorted(a)==sorted(b))
    
print(are_anagram("elbow","below"))
#################################################
'''input1=input(int("Enter the number:"))
if abs(input1)<10:
    return -1
else:
    input2=abs(input1)//10
    set_digit=input2 % 10
    return set_digit 
'''