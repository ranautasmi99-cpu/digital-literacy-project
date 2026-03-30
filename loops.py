from ast import Add


count = 1 
while count<=5 :
    print("hellow")
    count +=1 



#program for odd number generation 
i =1
while i<= 10 :
    print(i)
    i+=2 #odd


#program to find even number genreraion
i = 0 
while i <=10:
    print(i)
    i += 2 # even

#program to print the natural numbers upto 20
i = 1
while i <=20 :
    print(i)
    i +=1
else: 
    print("the code is exausted")

#break statement 
list = [10,20,30,40,50,60 ,70]
count = 1 
for i in list:
    if i == 50:
        print ("item matched")
        break                 #the break keyword is used to bring the program control out of the loop
    else:                     #it will break the entire loop when i reaches 50 and wont allow to print rest of the numbers

        count = count +1 
print("found at ",count,"location ")  


# countinuous statwment 
for i in range (1,8):
    if i<6:          #if condition ke andar jo bhi valuse aaayegi continue usse skip ksr dega
        print("skip")
        continue
    print(i)


#passs statement 
li = ["a","e","i","o","u"]
for i in li:
    if (i =="a"):
        pass #it stops to print the letter a and allow to print the rest
             #pass block doesnt have any code hence nonthing to do 
    else:    
        print(i)


#print numbers from 1 to 100
i = 1
while i <= 100:
    print (i)
    i+= 1


#print the numbers from 100 to 1
i = 100
while i>=1:
    print(i)
    i-=1

#print the multiplication table of a number n
n = int(input("enter a number:"))
i = 1
while i<=10:
    print(n*i)
    i+=1

#to print the list using for loop
list = [1,2,3,4,5,6,7,8,9]
list.append(23)
print("the new list of elements are", list)
#for el in list:
   # print(el)
    
#write a program to add 10 consecitive numbers starting from 1 using the while loop
count = 0  #initialize the counter
sum = 0  #initialize sum to zero 
while count <=10:            #test condition if true
    sum = sum+ count         #add sum + count
    count = count+1          #inc the value of count by 1
    print ("sum of first 10 numbers are :", sum)     

#write a program to find the sum of the digits
n= int(input("enter a number:"))
sum = 0
rem = 0
while n>0:
    rem = n%10 #remainder extract the last digit of number
    sum = sum + rem
    n = n // 10      
     
print("sum of the digits are:",sum)


#write a program to to display the reverse of the number entered
num = int(input("enter a number:"))
x = num
reverse = 0
rem = 0 
while num>0:
    rem = num%10
    reverse = reverse*10 +rem
    num = num // 10

print("the reverse of the enterned number:",x,"is",reverse)
    


# write a program to print the square of first five numbers
i = 1
while i <= 5:
    square = i *i
    print("the square of",i,"is", square)
    i+=1


#write a program to print even numbers from 0 to 10 and find their sum 
i=0
sum =0
while i<=10:
        print(i)
        sum = sum +i
        i+=2
        
print("sum is:",sum)        



#write a program to calculate the sum of numbers from 1 to 20 which are not divisible by 2,3or 5
sum = 0 
print("numbers from 1 to 20 which are not divisible by 2, 3,and5")
for i in range (1,20):
    if i%2==0  or  i%3==0 or  i%5==0:
        continue
    print(i)
    sum = sum +i
print("the sum of the numbers 1 to 20 which are not divisible by 2,3 or 5 is:",sum)


lst = []

n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input("Enter element: "))
    lst.append(val)

search = int(input("Enter element to search: "))

found = False
for i in range(len(lst)):
    if lst[i] == search:
        print("Element found at position:", i + 1)
        found = True
        break

if not found:
    print("Element not found")



def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


n = int(input("Enter number of terms: "))
print(fibonacci_iterative(n), end=" ")



#print the sum of the square of first natural numbers
lst = [1,2,3,4,5]
sum = 0
for i in lst:
    sum += i
print("Sum of list elements:", sum)


num = int(input("enter a number "))
result = 0 #result =[]  You’re printing list, not reversed number
while num>0:#while loop kayuki for loop mai tab tak run karega jab tak condition true hai
    t = num%10 
    result = result*10 + t #result = result.append(t)  This is incorrect for reversing a number. You should multiply the current result by 10 and add the last digit to it. 
    num=num//10
print(result)     

num = int(input("enter a number"))
org = num
rev = 0
while num>0:
    t = num%10
    rev = rev*10 + t
    num = num//10
print(rev)
if rev == org:
    print("the number is palindrome")
else:
    print("it is not a palindrome")

list = [1,2,3,4]
result = []
for num in list:
     num = num**2
     result.append(num)
print(result)


a = [1,2,3]
b = [4,5,6]

result = a+b
print(result)

#Store first 10 natural numbers in a list using loop
num = 1
result =[]
while num<=10:             
    result.append(num)
    num+=1
print(result)

#Add two lists element-wise (Dot Product)

a = [1,2,3]
b = [4,5,6]
dot_product = 0
for i in range(len(a)):
    dot_product += a[i] * b[i]
print("Dot product of", a, "and", b, "is:", dot_product)
    

a = [1,2,3]
b = [4,5,6]
sum = 0
for i in range(len(a)):
    mul = a[i] * b[i]
    sum += mul
print("Sum of", a, "and", b, "is:", sum)