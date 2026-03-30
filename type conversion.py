#type conversion 
#1)dtring to int base conversion
#print(int("10001",2))

#2)int to float conversion 
#year = 2025
#print(float(year))

#3)int to complex data type conversion
#print(complex(1,2))

#4) float to complex data type conversion 
#print(complex(1.1,22.2))

#print(str(11))
#print(str(11.23))

# tuple to list conversion
languages = ("hindi","punjabi","pahadi", "gujrati")
print("datatype of languages:",type(languages))
  
value= list(languages)
print(value)
print("datatype of value:", type(value))

#program to convert ASCII Value to characters 
a = chr(65)#converts ASCII value 65to upper case A
b = chr(97)# converts to ASCII value 97 to lower case a

print(a)
print(b)

# addition of two numbers using mixed data type 
num1= 22
num2= 15.5
print("datatype of num1:", type(num1))
print("datatype of num2:",type(num2))

add = num1+num2
print("value of addition=",add)
print("datatype of add:",type (add))#the result will be in float 
