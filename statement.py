#IF-ELSE statement range function
n = int(input("enter the number up to which you want to print the natural numbers"))
for i in range(0,n):
    print(i)

    #LOOPS
#program to print all the letters in the given string using for loop
statement = str(input("enter your name:"))
for x in statement: #x is a looping control variable
    print((x), end=" " )# print all the leters in the string 5



#program to calculate sum of n numbers using for loop
n = int(input("enter a number"))
sum = 0
for i in range(1,n):# eange(1,n,1)
    sum+= i  #sum = sum  + i 1,2,3,4....n
print(sum)


#program to print the reverse of  the natural numbers using for loop
num = range(15,1,-1) #range function starts with 15, stops with 1 and the update value is -1
for x in num: # control variable x fetches each value from the range function
    print(x)
    