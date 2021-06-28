//Create a lambda function that multiplies argument x with argument y

mul = lambda a,b: a*b
print(mul(3,5))

OUTPUT:
15

//Write a Python program to create Fibonacci series to n using Lambda

def fib(n):
	a= [0, 1]
	any(map(lambda _: a.append(sum(a[-2:])),range(2, n)))
	return a[:n]   
print(fib(5))

OUTPUT:
[0, 1, 1, 2, 3]

//Write a Python program that multiply each number of given list with a given number 
a=[4, 5, 6, 7, 8]
print("Original list:", a)
x=3
print("Given number:", x)
l1=map(lambda number:number*x,a)
print(' , '.join(map(str,l1)))

OUTPUT:
Original list: [4, 5, 6, 7, 8]
Given number: 3
12 , 15 , 18 , 21 , 24

//Write a Python program to find numbers divisible by 9 from a list of numbers 
a = [9,18,27,45,54,35,40]
print("Orginal list:",a)
res = list(filter(lambda x: (x % 9 == 0 ), a)) 
print("\nNumbers of the above list divisible by nine:",res)

OUTPUT:
Orginal list: [9, 18, 27, 45, 54, 35]
Numbers of the above list divisible by nine: [9, 18, 27, 45, 54]
  
//Write a Python program to count the even numbers in a given list of integers 
a = [1, 2, 3, 5, 7, 8, 9, 10]
print("Original arrays:",a)
even = len(list(filter(lambda x: (x%2 == 0) , a)))
print("\nNumber of even numbers in the above array: ", even)

OUTPUT:
Original arrays: [1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array:  3  
  
