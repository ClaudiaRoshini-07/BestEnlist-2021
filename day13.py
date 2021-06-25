//Write a Python program for all the cases which can check a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

import re
pat="[a-zA-Z0-9]{1}"
a=input("Enter the  string: ")
if(re.search(pat,a)):
    print("String Found")
else:
    print("String Not Found")

    
OUTPUT:
Enter the  string: Tina
True

//Write a Python program that matches a word containing 'ab'.

import re
pattrn="[\w*a\w*b.\w*]"
a=input("Enter the String :")
if(re.search(pattrn,a)):
    print("String contains ab")
else:
    print("String does not contain ab")
    
OUTPUT:
Enter the String :ababa
String contains ab

//Write a Python program to check for a number at the end of a word/sentence.

import re
pattern=r".*[0-9]$"
b=input("Enter the string :")
if(re.search(pattern,b)):
    print("Contains number at the end of the string")
else:
    print("Does not contain number at the end of the string")

OUTPUT:
Enter the string :tina7
Contains number at the end of the string

Enter the string :tina
Does not contain number at the end of the string

//Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string

import re
a=r"[0-9]{1,3}"
b=input("Enter the string: ")
y=re.finditer(a,b)
for i in y:
    print(i.group(0))

Output:
Enter the string: tina mark 987
987 

//Write a Python program to match a string that contains only uppercase letters

import re
r=input("Enter the String:")
patterns = '^[A-Z]*$'
if re.search(patterns, r):
      print("Found ")
else:
      print("Not Found")


 OUTPUT:
Enter the String:HELLO
Found
Enter the String:hello
Not Found



      

