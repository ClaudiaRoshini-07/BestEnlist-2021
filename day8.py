// Python script to merge two Python dictionaries

dict1 = {'nisha': 100, 'tina': 200}
dict2 = {'dani': 300, 'vijay': 200}
d = dict1.copy()
d.update(dict2)
print(d)

OUTPUT:
  {'nisha': 100, 'tina': 200, 'dani': 300, 'vijay': 200}
  
//Write a program to sort the value from descending to ascending in list and
convert it in to a set.

l1=[1,9,7,8,3,6,4]
print("List before sorting : ",l1)
l1.sort()
print("List after sorting : ",l1)
listset=set(l1)
print("After converting to set : ",listset)


OUTPUT:

List before sorting :  [1, 9, 7, 8, 3, 6, 4]
List after sorting :  [1, 3, 4, 6, 7, 8, 9]
After converting to set :  {1, 3, 4, 6, 7, 8, 9}

//Write a Python program to list number of items in a dictionary key and sort the list with the help of a function 

dic={'cathy':1,'tina':2,'john':10,'blacky':7}
a=dic.keys()
y=list(a)
y.sort()
print("After Sorting keys using function ")
print("{",end="")
for i in range(len(y)):
    print(y[i],":",dic[y[i]],",",end="")
print("}")

OUTPUT:

After Sorting keys using function
{blacky : 7 ,cathy : 1 ,john : 10 ,tina : 2 ,}

///Write a Python program to list number of items in a dictionary key and sort the list without the help of a function 

dic={'cathy':1,'tina':2,'john':10,'blacky':7}
a=dic.keys()
b=list(a)
z=[]
for a in range(len(b)): 
    for j in range(a+1,len(b)):
        if(b[a]>b[j]):
            temp=b[a]
            b[a]=b[j]
            b[j]=temp


print("Keys without function ")
print("{",end="")
for a in range(len(b)):
    print(b[a],":",dic[b[a]],",",end="")
print("}")

OUTPUT:
{blacky : 7 ,cathy : 1 ,john : 10 ,tina : 2 ,}

//Write a Python program to get a string from a given string (user input) and change the first occurrence of the word to a user specified input.

a=input("Enter the string :")
b=input("Enter the substring :")
c=input("String to be replaced :")
d=a.split()
for i in range(len(d)):
    if(d[i]==b):
        d[i]=c
        break
str=""
for i in d:
    str+=i
    str+=" "
print("After replacing : ",str)

OUTPUT:

Enter the string :Hello CSE
Enter the substring :Hello
String to be replaced :Hi
After replacing :  Hi CSE

//Write a Python program to get a string from a given string where all occurrences of its first char have been changed to capital letter.

x=input("Enter the string: ")
y=x[0]
z=y.upper()
d=x.replace(y,z)
print("After replacing the first charcter:",d)

OUTPUT:
Enter the string: hello
After replacing the first charcter: Hello

//Write a Python program to find the repeated items of a list

list=[1,2,3,1,2,3]
list1=[]
list2=[]
for i in list:
    if(i not in list1):
        list1.append(i)
    else:
        list2.append(i)
print("Repeated items :",list2)

OUTPUT:
Repeated items are : [1, 2, 3]

//Write a Python program to check the sum of three elements and divided by a value which is given as an input by the user

a=4
b=5
c=6
sum=a+b+c
m=int(input("Enter number to be divide"))
print("The sum afters dividing  : ",sum/m)

OUTPUT:
Enter number to be divide5
The sum afters dividing  :  3.0

//Write a Python program to find the Mean,median,mode among three given numbers

import statistics
a=15
b=25
c=35
mean=(a+b+c)/3
l=[a,b,c]
print("Mean  :",mean)
print("Median:  ",statistics.median(l))
print("Mode : ",statistics.mode(l))

OUTPUT:
Mean  : 25.0
Median:   25
Mode :  15

//Write a Python program to swap cases of a given string

def swap(str1):
   str = ""   
   for i in str1:
       if i.isupper():
           str += i.lower()
       else:
           str += i.upper()           
   return str
print(swap("Tina"))
print(swap("John"))
print(swap("cATHY"))	

OUTPUT:
tINA
jOHN
Cathy

//Write a program to convert an integer to binary & octa decimal

x=15
print("After converting to Integer : ",x)
print("After converting to Binary : ",bin(x))
print("After converting to Octal : ",oct(x))

OUTPUT:
After converting to Integer :  15
After converting to Binary :  0b1111
After converting to Octal :  0o17
