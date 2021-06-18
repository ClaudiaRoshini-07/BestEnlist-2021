//Create a function getting two integer inputs from user. & print the following:

Addition of two numbers is +value

Subtraction of two numbers is +value

Division of two numbers is +value

Multiplication of two numbers is +value

Here the value represents math function associated

PROGRAM:
def add(a,b):
	add=a+b
	return add
def sub(a,b):
	sub=a-b
	return sub
def mul(a,b):
	mul=a*b
	return mul
def div(a,b):
	div=a/b
	return div
m=int(input("Enter the first no:"))
n=int(input("Enter the second no:"))
print("Addition of two no is:",add(m,n))
print("Subraction of two no is:",sub(m,n))
print("Multiplication of two no is:",mul(m,n))
print("Division of two no is:",div(m,n))

OUTPUT:
Enter the first no:6
Enter the second no:3
Addition of two no is: 9
Subraction of two no is: 3
Multiplication of two no is: 18
Division of two no is: 2.0
  
//. Create a function covid( ) & it should accept patient name, and body temperature, by default the body temperature should be 98 degree

PROGRAM:
def covid(pat_name,body_temp=98):
	print("patient name:",pat_name)
	print("patient temperature:",body_temp)
covid("tina")

OUTPUT:
patient name: tina
patient temperature: 98
