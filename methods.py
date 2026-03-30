#now let us see the way two join different lists using extend() method
list1 = ["python", "r" , "julia"]
list2 = [1,2,3]

list1.extend(list2) # both the list will add up
print(list1)


#way to remove an element from a list using the value
flowers = ["rose","sunflower","lotus","lily"]
flowers.remove("sunflower")# remove method
print(flowers)
               # or 
# way to delete an element from the list using the index
brand = ["h&m" , "lv", "ysl", "dior"]
del brand[0]  #del operator
print(brand)

#inserting an element using the index value
animals = [ "cat","dog", "cow"]
animals.insert(0,"horse")  #insert() method
print(animals)
animals.insert(2,"elephant")
print(animals)


# way to reverse the list elements using reverse () method
fruits = ["orange","kiwi", "apple","mango"]
fruits.reverse() #reverse method 
print(fruits)


# way to sort the list elements using sort() method
fruits = ["orange","kiwi", "apple","mango"]
fruits.sort()
print(fruits)

#print using string formating
print ("1 love {0} and {1}".format("python", "java"))

print ("1 love {1} and {0}".format("python", "java"))

print("hello {name} , welcome to {place}".format(name="john", place="paris"))


#string split
text = " i love programming"
x = text.split()  #split method where it will split the string into a list
print(x)


#sum of two numbers using map & input function 
#getting multiple input with ',' separator
a, b = map(int, input("Enter two numbers: ").split(','))
print(a+b)
#need to put comas while entering hte numbers






