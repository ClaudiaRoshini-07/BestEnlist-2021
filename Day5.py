//Write a program to create a list of n integer values

b= list(range(1,7))
print(b)

OUTPUT:
[1, 2, 3, 4, 5, 6]

//Add an item in to the list (using function)

b= list(range(1,7))
b.append(8)
print(b)

OUTPUT:
[1, 2, 3, 4, 5, 6, 8]

//Delete (using function)

b= list(range(1,7))
b.pop(1)
print(b)

OUTPUT:
[1, 3, 4, 5, 6]

//Store the largest number from the list to a variable

b= [1,2,3,4,5,6]
c=max(b)
print(c)

OUTPUT:
6

//Store the Smallest number from the list to a variable

b= [1,2,3,4,5,6]
c=min(b)
print(c)

OUTPUT:
1

//Create a tuple and print the reverse of the created tuple 

tup1=(1,2,3,4,5)
a=tup1[::-1]
print(a)

OUTPUT:
(5, 4, 3, 2, 1)

//Create a tuple and convert tuple into list 

tup1=(1,2,3,4,5)
a=list(tup1)
print(a)

OUTPUT:
[1, 2, 3, 4, 5]


