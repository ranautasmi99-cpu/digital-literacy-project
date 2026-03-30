#WAF to print the length of a list (list is the parameter )
names = ["asmi","shally","pradeep", "ranaut"]
print(len(names))
            #or
def print_len(list):
    print(len(list))
     
print_len(names)



#WAF TO PRINT THE ELEMENTS OF A LIST IN A SINGLE LINE
def print_items(list):
    for items in list:
        print(items,end=" ")

print_items(names)



#WAF TO FIND THE FACTORIAL OF A n (n is the parameter)
n= 5 
fact= 1 
for i in range (1,n+1):
    fact*=i
print(fact)
 
                       #or
def cal_fact(n):
    fact=1 
    for i in range(1,n+1):
        fact*=i
    print(fact)

cal_fact(5)



# WAF TO CANVERT USD TO INR
def converter(usd_val):
    inr_val = usd_val *83
    print(usd_val,"USD=", inr_val,"INR")

converter(2)


# to change of an item value or to update the list element
list = ["asmi","ranaut",19 ,2005 ]
print("value available in index 3 :", end=" ")
print(list[3])
list[3]= 2006 # it updated the third element 
print("new value available in index 3:" , end=" ")
print(list[3])


#mr. rama buys a 2BHK luxuary in hyderabad for the cost of rs A and he had gone for interior decoration with Rs B cost . luckily in his terrotory government  has announced a special economic zone (SEZ).
#  the demand for the flats in that area boomed up by the white coller &golden collar professional . if he sells the flat for Rs .Z what is his gain in % ? 
# write a python program to compute the profit in percentage ? input format : three integers seperated by space . output format :the profit is:
def profit_percentage(A,B,Z):
    cost_price = A + B
    selling_price = Z
    profit = selling_price - cost_price
    profit_percent = (profit / cost_price) * 100
    print("The profit is:", profit_percent,"%")

profit_percentage(5000000, 200000, 6000000)


                                #or
#getting multiple input with spaces 
# #profit calculation 
A,B,Z = map(int,input().split())
r = ((Z-(A+B))/(A+B))*100
print("the profit is:", round(r,2),"%")    



#wap to find the sum of first n natural numbers
n = 1
sum = 0
n = int(input("enter a number:"))
while n>=1:

    sum = sum +n
    n = n-1 
print("the sum of first n natural numbers is:",sum)



#wap to find the factorial of first n numers
n = int(input("enter a number:"))
fact = 1
while n>=1:
    fact = fact * n
    n = n-1
print("the factorial is:",fact)


# 1. Create variables
a = 10                  # Integer
b = 5.5                 # Float
c = "20"                # String
d = [1, 2, 3, 4, 5]     # List

# 2. Add integers and convert to float
sum_val = float(a + 5)

# 3. Concatenate strings and convert to integer
s1 = "12"
s2 = "34"
concat_int = int(s1 + s2)

# 4. Convert list to tuple
tup = tuple(d)

# 5. Float to string and join
new_string = str(b) + " is a float"

# 6. Convert string number to integer
num = int("45")

# 7. Float → int → string
val = str(int(9.8))

# 8. Print values and data types
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(sum_val, type(sum_val))
print(concat_int, type(concat_int))
print(tup, type(tup))
print(new_string, type(new_string))
print(num, type(num))
print(val, type(val))
