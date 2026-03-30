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