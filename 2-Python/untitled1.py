# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 15:09:13 2025

@author: maith
"""

# -- coding: utf-8 --
"""
Created on Fri Apr 18 08:23:14 2025

@author: ptlpr
"""
import re
#1..(dot). matches any character except newline
print(re.findall(r"a.c","abc aac acc adc a.c"))
#output:['abc', 'aac', 'acc', 'adc', 'a.c']
'''
a is trying to match a
. -> match any one character [except new line]
c -> matches letter c
so ovrerall its looking for three character string where 
the first letter is 'a'
the last letter is 'c'
the middle can be any character
abc (a + any character b + c)
acc (a + any character c + c)
aac (a + any character a + c)
adc (a + any character d + c)
a-c (a + any character - + c)

'''

#2. ( caret) - matches start of string
print(re.findall(r"^Hello","Hello World\nHello Python"))
#output:[Hello]
'''
^ -> this is the caret , and it means:
^Match the following pattern only if it appears at the 
Hello -> this is the actual text you're trying to match
so "hello means:" 
"match the word 'hello' only if it is at the begining of
input:Hello World\nHello Python"
 "Hello World"
 "Hello Python" + on a new line
 But since the ^ anchor only applies to the beginning
 of the whole string , it will match only the first
 "hello", not the second one
 output:['Hello']
 '''
 
#3. (Dollar) - matches end of string
print(re.findall(r"Python$","Hello Python"))
#output: ['python']

'''
Python ->this is the text you're trying to match
$ -> this means
"match this ** only if it appear at the end of the string"
so python means:
"match the word 'python' only if it's at the very end of the string"
'''

#try this  
re.findall(r"Python$","HEllo Python Developer")
#output:[]

#4. * (asterisk) - 0 or more of the preceding char
print(re.findall(r"ab*c","ac,abc,abbc,abbbc"))
#output:['ac','abc','abbc','abbbc']

'''
Patterns: ab*c
the pattern uses the asterisk *, which is one of the no breakdown:
a -> match the character 'a'
b* -> match zero or more 'b' characters
c -> match the character 'c'

word     Matches ab*c?     Why?
ac       yes               'b' appears zero times
abc      yes               'b' appears one times
abbc     yes               'b' appears two times
abbbc    yes               'b' appears three times
'''

#5.+ (plus) - 1 or more of preceding character
print(re.findall(r"ab+c","ac abc abbc abbbc"))
#output : ['abc','abbc','abbbc']

'''
ab +c
this pattern uses the plus + quantifier
which is closely related to the * we discussed before
BREAKDOWN:
a -> Match the character 'a'
b+ ->Mathc one or more 'b' character
c -> Match the character 'c'
so the full pattern matches
'a' followed by at least one 'b', followed by 'c'
let's check each word:
    
"ac" 
no 'b' between 'a' and 'c'.b+ requires at least one
"abc"
One 'b' -> matches 'ab+c'
"abbc"
two 'b's -> matches 'ab+c'
"abbbc"
three 'b's -> matches 'ab +c'
'''
#6. ? (question) - 0 to 1 of the preceding character
print(re.findall(r"ab?c","ac abc abbc abbbc"))
#output:['ac','abc']

'''
Pattern: ab?c
BREAKDOWN:
a -> Match the character 'a'
b? ->Mathc zero one  'b' character
c -> Match the character 'c'

so the full pattern matches
'a' followed by at most one 'b', followed by 'c'
let's check each word:
    
    word     Matches ab*c?     Why?
    ac       yes               'b' appears zero times(allowed)
    abc      yes               'b' appears one times(allowed)
    abbc     No               'b' appears two times(not allowed)
    abbbc    No               'b' appears three times(to many)
'''

#7 . {} (curly brace) - exact or range of repetitions
print(re.findall(r"ab{2}c","ac abc abbc abbbc"))
#output:['abbc']
'''
Pattern: ab{2}c
BREAKDOWN:
a -> Match the character 'a'
b? ->Mathc exactly 2 'b' character
c -> Match the character 'c'

so this regex will only matche
'a' followed by exactly 2 'b's, followed by 'c'
i.e teh string "abbc"
    
    word     Matches ab{2}c?     Why?
   
    abc      yes              only 1 b -> needs 2
    abbc     No               exactly 2
    abbbc    No               three b's -> too many
    abbbbc   no               four b's  -> too many
'''

#8 . [] (square bracket) - either b or c character set
print(re.findall(r"a[bc]d","abd acd aad aed"))
#output:['abd','acd]

'''
Pattern: a[bc]d
BREAKDOWN:
a -> Match the character 'a'
[bc] ->Mathc exactly one character, and it must be either 'c' or 'b'
d -> match the character 'd'
c -> Match the character 'c'

so this regex will only matche
'a' followed by exactly 2 'b's, followed by 'c'
i.e teh string "abbc"
    
    word     Matches ab{2}c?     Why?
   
    
'''
#9. [^](negated set) - not in the set
print(re.findall(r"a[^bc]d","aad aed acd abd"))
#output:['aad', 'aed']
'''
Pattern: a[^bc]d
Breakdown:
a-> Match the character 'a'
[^bc]->Match any one character except 'b' or 'c'
The caret ^ inside square brackets negates the set.
d-> Match the character 'd'
so this pattern matches:
'a' followed by any character that is not b or c, followed
'''