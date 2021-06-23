//1.	Create a python module with list and import the module in another .py file and change the value in list

FILE NAME:list.py
 l1=[64,12,16,18] 
  
 FILE NAME: list2.py
 import list1 as li
s=[]
s=li.l1
for i in range(len(s)):
  s[i]+=2
print(s)

OUTPUT:
[66, 14, 18, 20]

//2.Install Panda package
//3.	Import a module that picks random number and write a program to fetch a random number from 1 to  100 on every run

import random
num=random.randint(1,100)
print(num)

OUTPUT:
  
85
1
89
69

//4.	Import sys package and find the python path
import sys,os
file=sys.argv[0]
path_name=os.path.dirname(file)
print(path_name)
