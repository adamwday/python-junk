#----------------------------------------------------------------------#
# This sample python code just so I can get a feel for coding in python.
#----------------------------------------------------------------------#

#------#
# MATH #
#------#
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

#---------#
# STRINGS #
#---------#
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

#-------------------#
# STRING PROPERTIES #
#-------------------#
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

#------------------#
# PRINT FORMATTING #
#------------------#
#Insert a variable into a print string
print 'this is a string'
z = '13.13'
print 'Place my variable here: %s' %(z)
#Print a floating point number and mandate at least 1 mininum character before
#the decimal and limit 2 places after decimal
print 'Floating point number: %1.2f' %(13.145)
#Insert a variable into a print string
print 'Convert to string %r' %(z)
#Using multiple % signs
print 'First: %s, Second: %s, Third: %s' %('hi!', 'two', 3)
#Using the string.format Method (preferred over example above)
print 'First: {x} Second: {y} Third: {x}' .format(x='inserted', y='two!')
#Python 3 example of above
print('One: {x}' .format(x='INSERT!'))

#------------------------#
# LISTS and LIST METHODS #
#------------------------#
#Assigning a list to a variable
my_list = [1,2,3]
my_list = ['string',23,1.2,'o']
#Get length of a list
len(my_list)
my_list = ['one', 'two', 'three, 4, 5']
#Grab the first element
my_list[0]
#Grab everyting after the first element
my_list[1:]
#Grab everything up to the third element
my_list[:3]
#concatenate STRINGS
'hello' + 'world'
#concatenate list with STRINGS
my_list + ['new item']
#Adding new elements to a list
my_list = my_list + ['permanent add']
#Appending methods
l = [1,2,3]
1.append ('append me!')
l
#Popping off (displaying) the last element permanently
l.pop()
#Popping off (displaying) the first element permanently
x = l.pop(0)
#Create a new list and reverse the ordere
new_list = ['a', 'b', 'c', 'd']
new_list.reverse()
new_list
#
l_1 = [1,2,3]
l_2 = [4,5,6]
l_3 = [7,8,9]
matrix = []
