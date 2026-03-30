#swap two numbers
a = 10
b= 7
c=0
c=a 
a=b
print(c)
print(a)

a = int(input("enter a value"))
b= int(input("enter a value"))
a,b = b,a
print("after swaping")
print("a",a)
print("b", b)

#area of circle 
a = float(input("enter a vaule"))
area = 3.14*a**2
print("area of circle is",area)


#simple calculator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)

choice = input("Enter operation (+, -, *, /): ")
if choice =="+":
    print("the sum is ",a+b)
elif choice =="-":
    print("the sub is :",a-b)
elif choice=="*":
    print("the product is ",a*b)
elif choice =="/":
    if b!=0:
        print("the div is",a/b)
    else:
        print("invalid")
else:
    print("invalid")


#Sum of Even Numbers Problem:

#Take a number n as input
#Print the sum of all even numbers from 1 to n
n = int(input("enter a number"))
sum = 0
for i in range(1,n+1):
    if n%2==0:
      sum+=i
      
print(sum)


#Count Digits
#🎯 Problem:
#Take a number and count how many digits it has
number = input("enter a digit")
n = len(number)
print(n)

n = int(input("enter a number"))
count= 0
while n>0:
    count+=1
    n//=10
print(count)