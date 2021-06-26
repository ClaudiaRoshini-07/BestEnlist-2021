//List down all the error types and check all the errors using a python program for all errors

//Indexerror
l=list(range(0,6))

try:

	print(l[8])
except:

	print("Error handled")
  
//ZeroDivisionError
  
try:

  x=2/0

  print(x)
except:

  print("Cannot divide by zero")
  
//ValueError
try:

  a=int(input("Enter the number"))
except:

  print("It is not a number")
  
//Design a simple calculator app with try and except for all use cases
  
 print("enter 1 for add,2 for subtraction,3 for multiply,4 for division")

try:

	choice=int(input("option:"))

if choice==1:

    first=float(input("Enter first number:"))
    
    second=float(input("Enter second number:"))
    
    print(first+second)
    
elif choice==2:
  
  first=float(input("Enter the first number:"))
  
  second=float(input("Enter the second number:"))
  
  print(first-second)
elif choice==3:
  
  first=float(input("Enter first number:"))
  
  second=float(input("Enter second number:"))
  
  print(first*second)
elif choice==4:
  
  first=float(input("Enter first number:"))
  
  second=float(input("Enter second number:"))
  
  print(first/second)
else:
  
  print("enter a valid integer")
except NameError:

print("Invalid input")
except SyntaxError:

print("Invalid input")
except TypeError:

print("Invalid input")
except AttributeError:

print("Invalid input")
except ValueError:

print("Invalid input")

//print one message if the try block raises a NameError and another for other errors

try:

	raise NameError("java")
except NameError:

	print("The Exception is handled")
  
//When try-except scenario is not required?
Whenever there is no need for error to be handled or whenever when we allow  the program to display the error,try-except scenario is not required.

//Try getting an input inside the try catch block
while True:

try:

    a=int(input("Enter the integer"))

    print("The integer you have entered is",a)

    break
except:

    print("Invalid integer")
