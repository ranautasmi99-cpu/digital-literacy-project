#An array stores multiple values of the same type under one name

import numpy as np

a = np.array([1, 2, 3, 4])
print(a)

#with list
a = [1, 2, 3]
b = []
for i in a:
    b.append(i * 2)
print(b)

#with arrays
import numpy as np
a = np.array([1,2,3])
b = a * 2
print(b)


from array import*
#Create first array
a = array('i', [1, 2, 3, 4])
#From first array create second
b = array(a.typecode, (i for i in a))
#print the second array items  
print("Items are: ")
for i in b:
    print(i)
#From first array create third
c = array(a.typecode, (i * 3 for i in a))
#print the third array items 
print("Items are: ")
for i in c:
    print(i)


#program to create input and output array
import numpy as np
x = np.arange(5) #generate array of elements from 0 to 4
y = np.empty(5) #generate empty array of size 5
np.multiply(x, 10, out=y) #multiply x by 10 and store in y
print(y)

 

#one dimentional arrays
import numpy as np
t = np.arange (5)
print(t)

y = t*2
print(y)

x = t*2 +1
print(x)

r = t**2    #This is used for:kinetic energy (v²),varianc , wave equations
print(r)
# or
n = np.square(t)
print(n)

sum = np.sum(t)
print(sum)

mean = np.mean(t)
print(mean)


#Working with TWO 1D arrays
#Element-wise multiplication
import numpy as np                    
a = np.array([1, 2, 3])
b = np.array([2,4,5])
c = a * b
print(c)     
#Examples:work = force × displacemen 
#  power = voltage × current
#energy = ½ m v²
# signal processing
#weighted sum
t = np.cross(a,b)
print(t)
#OR
z = np.sum(a*b)
print(z)

from numpy import*
a = array(['abc', 'bcd', 'cde','def'],dtype=str)  
print(a)


#Creating an Array:numpy-linspace(
from numpy import*
# Syntax = linspace(start, stop,n)
a = linspace(0, 10,5)
#Create an array ‘a’ with starting element 0 andending10.  This range is divide into 5 
#equalparts
print(a)
#Hence, items are 0, 2.5, 5, 7.5,10


#Creating an Array:numpy-arange()

#Syntax arange(start, stop,stepsize)
#xample-1 arange(10) Produces itemsfrom 0 -9
#Example-2 arange(5,10) Produces itemsfrom 5 -9
#Example-3 arange(1, 10,3) Produces itemsfrom 1, 4,7
#Example-4 arange(10, 1,-1) Produces itemsfrom [10 98 7 6 5 4 3 2]
#Example-5 arange(0, 10,1.5) Produces [0. 1.53. 4.56. 7.5 9.]


#Comparing Array

from numpy import*
a = array([1, 2,3])
b = array([3, 2,3])
c = a>b  
print(c)
print("any(): ",any(c))    #any(): Used to determine if any one item of the array isTru
print("all(): ",all(c))    #all(): Used to determine if all items of the array areTru
if (any(a >b)):
    print("a contains one item greater than those ofb")
elif (all(a >b)):
    print("all items of a are greater than those ofb")
else:
    print("all items of a are not greater than those ofb")


#Program-4: To understand the usage of wherefunction
from numpy  import*
a = array([1, 2, 3],int)
c = where(a % 2 == 0,a,0)  #where(): used to create a new array based on whether a given condition is True orFals
print(c)
#Syntax: a = where(condition, exp1,exp2)
#If condition is True, the exp1 is evaluated, the result is stored inarray
#a, else exp2 will beevaluate



import numpy as np
A = [4, 8, 7]
B = [5, -4, 8]
print("The input arrays are :\n","A:",A ,"\n","B:",B)
Res= np.subtract(A,B)
print("After subtraction the resulting array is :",Res)

import math 
true_value = cos(3.14/3)
