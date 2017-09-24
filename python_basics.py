########################################################################
# This sample python code just so I can get a feel for coding in python.
########################################################################

########
# MATH #
########
#Importing division from python 3.0
from __future__ import division

#Addition
2+2
#Subtraction
2-2
#Multiplication
2*2
#Division using floating point (for python 2.x only)
2.0/2
#Division using float to give us 2.0/2 (for python 2.x only)
float(2)/2
#Calculating two to the power of 3 (2^3)
2**3
#Adding an equation using an order of operations.
(2+10)*(10+3)
#Adding a label to something using "="
a = 5
#Using the variable "a"
a + a
#Simple tax calculation using variables.
my_income = 100
tax_rate = 0.1
my_taxes = my_income*tax_rate
my_taxes
print my_taxes

###########
# STRINGS #
###########
from __future__ import print_function
'Hello'
'This is also a string'
"This is also a string in double quotes because I'm using an apostrophe in "I'm""
#Printing a string
print ('hello world 1')
print ('hello world 2')
#Printing a string with multiple lines.
print ('here is some text where I am \n wrapping text into multiple lines with \n')
#Using the length function to count characters in a string
len('hello world')
#Assign a label and create a variables
s = 'Hello World'
print s
s
#Grabs the 2nd letter of variable 's'
s[1]
#Grabs everything from the 1 index (second letter) onwards from hello world
s[1:]
#Grab everything up to the 3rd index (not including fourth letter)
s[:3]
#Grab everything
s[:]
#Grab one index behind zero (last letter)
s[-1]
#Grab everything but the last letter
s[:-1]
#Grabs everything in step sizes of 1
s[::1]
#Grabs everything in step sizes of 2
s[::2]
#Print output in reverse
s[::-1]
#####################
# STRING PROPERTIES #
#####################
#Add 'Hello World' to another string
s = s + 'concatenate me!'
#Call letter as a variable
letter = 'zz'
letter
letter*10
#Create a variable for string
s = 'Hello'
#Method to make uppercase string
s.upper()
#method to make lowercase string
s.lower()
#split string by letter 'e'
s.split('e')
