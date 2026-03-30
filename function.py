#defining the function ( to reduce reduntancy we use function)
def func(name):
    print("hi",name)

#calling the function
func("frind")



#sum of two numbers 
def sum(a,b):
    print("the sum is ",a+b)

#calling the function
sum(3,7)





#finding the absolutee value using a function
#without paramater and without the return value 

def absolute_value():
    """this function returns the absolute 
    value of the enterned number"""
    num = int ( input("enter the number either +ve or -ve:"))
    if num>=0:
        print("the absolute value is : ",num)
    else:
        print("rhe absolute value is:-",num)
#driver code
absolute_value()  #function call





#finding the absolutee value using a function
#with paramater and without the return value 

def absolute_value(num):
    """this function returns the absolute 
    value of the enterned number"""
    
    if num>=0:
        print("the absolute value is : ",num)
    else:
        print("rhe absolute value is:",-num)
#driver code
n = int ( input("enter the number either +ve or -ve:"))
absolute_value(n)  #function call






 #finding the absolutee value using a function
#with paramater and with the return value 





#average of 3 numbers
def average(a,b,c):
    print("the average is:", (a+b+c)/3)
    
a= int(input("enter number 1"))
b=int(input("enter the number 2"))
c = int(input("enter the number 3"))
average(a,b,c)

              #or

#average of 3 numbers
def average(a,b,c):
    print("the average is:", (a+b+c)/3)
    return (a+b+c)/3
    
average(1,2,3)


#defining a function to calculate LCM with default values
def calculate_lcm(x=3, y=2):
    #selecting the greater number
    if x>y:
        greater = x
    else:
        greater = y
    while(True):
        if (greater % x ==0) and (greater % y==0):  #if both of the numberss are divisible by each other
            lcm = greater# LCM is the greatest number
            break
        greater +=1
    print("the LCM of",x,"and",y,"is",lcm)
    return lcm 

#driver code
# taking input from users
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
#printing the result for the users
print("the LCM OF",num1,"and",num2,"is:", calculate_lcm(num1,num2)) 


#python program to find GCD of two numbers

#define a function
def calculate_gcd(x,y):
    """this function returns the GCD of the two numbers"""
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if((x % i==0) and (y % i==0)):
            gcd = i
    return gcd
#driver code
x = int(input("enter the first number:"))
y = int(input("enter the second number:"))

print("the GCD of",x,"and",y,"is:", calculate_gcd(x,y))
print("the GCD of",x,"and",y,"is:", calculate_gcd(y,x))


#function definition
def add(a,b=5,c=10):
    """this function returns the sum of three numbers"""
    s = a + b + c
    return s 
#driver code
#function call method
print(add(b=100,c=15,a=20))#keyword argument 

#function call method 2
print(add(a=100)) #keyword argument with default values



#sum of n numbers
def add(*b):
    result = 0
    for i in b:
        result += i
    return result
#driver code
#function call method 1
print("the sum is:", add(10,20,30,40,50))

#function call method 2
print("the sum is:", add(10,20,30))



#arbitary keyword arguments
#function to diaplay course details 
def course_details(**a):
    print("course details are:")
    for i in a.items ():
        print (i)
#function call
course_details(course_name="python", course_duration="3 months", course_fee=15000)


#variable length arguments
def calc(*args):  #by using the * later i can add as many numbers as i want 
    s = 0 
    print("the number are as follows:")
    for num in args:
        print(num , end=" ")
        s += num
    return s 

total = calc(10,20 )
print("the total is:", total)
total = calc(10,20,30,40,50)
print("the total is:", total)


#the return statement 

#write a function calc_distance (x1,x2,y1,y2) that returns the distance between two points (x1,y1) and (x2,y2)
#the formulla to calculate the distance is d = sqrt((x2-x1)^2 + (y2-y1)^2)
import math
def calc_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance
#driver code
x1 = float(input("enter x1:"))
y1 = float(input("enter y1:"))
x2 = float(input("enter x2:"))
y2 = float(input("enter y2:"))
print("the distance between the points is:", calc_distance(x1, y1, x2, y2))




#recursive function
def sum(n):
    if n > 1:
        return n + sum(n - 1)
    return 1

num = int(input("enter the number:"))
print("the sum is:", sum(num))


#factorial of a number using function
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
num = int(input("enter the number:"))
print("the factorial is:", fact(num))




    



