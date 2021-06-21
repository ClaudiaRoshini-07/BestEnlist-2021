//Write a program to loop through a list of numbers and add +2 to every value to elements in list

l1=[1,2,3,4,5]
l2=[]
for j in range(0,len(l1)):
	l2.append(l1[j]+2)
print(l2)

OUTPUT:
 [3, 4, 5, 6, 7]

//Write a program to get the below pattern
54321
4321
321
21
1

a=int(input("Enter the no of rows:"))

for i in range(0,a+1):

for j in range(a-i,0,-1):

    print(j,end='')

print()

//	Python Program to Print the Fibonacci sequence

def fibo(n):

	if n<=1:

    		return n

	else:

   		 return fibo(n-1)+fibo(n-2)
fibo_terms=int(input("Enter the no:"))

if fibo_terms<=0:

	print("enter a valid no")
else:

	print("fibonacci sequence:")

for i in range(fibo_terms):

    print(fibo(i))
    
OUTPUT:
Enter the no:5
fibonacci sequence:
0
1
1
2
3

//Explain Armstrong number and write a code with a function

n=int(input("Enter the no:"))
s=0
temp=n
while(temp>0):
  val=temp%10
  s+=val**3
  temp=temp//10
if(n==s):

	print("the no is an armstrong number")
else:

	print("the no is not an armstrong number")
  
 OUTPUT:
  
  Enter the no:121
the no is not an armstrong number

//Write a program to print the multiplication table of 9

n=9
for i in range(1,11):
	print(n,"x",i,"=",n*i)
  
OUTPUT
9 x 1 = 9
9 x 2 = 18
9 x 3 = 27
9 x 4 = 36
9 x 5 = 45
9 x 6 = 54
9 x 7 = 63
9 x 8 = 72
9 x 9 = 81
9 x 10 = 90

//Check if a program is negative or positive

n=int(input("Enter the number:"))
if n>0:
	print("the no is positive")
else:
	print("the no is negative")
  
OUTPUT:
Enter the number:2
the no is positive

//Write a program to convert the number of days to ages

d=int(input("enter the no of days:"))
years=int(d/365)
print("Days to years=",years)

OUTPUT:
enter the no of days:378
Days to years= 1

//Solve Trigonometry problem using math function write a program to solve using math function

import math
x=math.pi/4
y=5
z=4
print("the cosine value of pi/4 is:")
print(math.cos(x))
print("the hypotenuse value of 4 and 5 is:")
print(math.hypot(y,z))

OUTPUT:
the cosine value of pi/4 is:
0.7071067811865476
the hypotenuse value of 4 and 5 is:
6.4031242374328485

//Create a calculator only on a code level by using if condition (Basic arithmetic calculation)

print("CALCULATOR")
a=input('Enter operator ')
b=int(input("Enter 1st number "))
c=int(input("Enter 2nd number "))
if(a=='+'):
    print(b+c)
elif(a=='-'):
    print(b-c)
elif(a=='*'):
    print(b*c)
elif(a=='/'):
    print(b/c)
else:
    print("Invalid operator")
    
  OUTPUT:
  CALCULATOR
Enter operator +
Enter 1st number 23
Enter 2nd number 32
55  
