// Python script to merge two Python dictionaries

dict1 = {'nisha': 100, 'tina': 200}
dict2 = {'dani': 300, 'vijay': 200}
d = dict1.copy()
d.update(dict2)
print(d)

OUTPUT:
  {'nisha': 100, 'tina': 200, 'dani': 300, 'vijay': 200}
  
// Python program to remove a key from a dictionary
  
dict1 = {'nisha': 100, 'tina': 200}
dict1.pop('nisha')
print(dict1)

OUTPUT:
  
{'tina': 200}

//Python program to map two lists into a dictionary

dict1={'nisha','tina','dani','vijay'}
dict2={90,78,85,46}
d3 = dict(zip(dict1,dict2))
print(d3)

OUTPUT:
  {'nisha': 90, 'tina': 78, 'dani': 85, 'vijay': 46}
  
//)  Python program to find the length of a set
  
dict1={'nisha','tina','dani','vijay'}
print("Length =",len(dict1))

OUTPUT:
Length = 4

//Python program to remove the intersection of a 2nd set from the 1st set

dict1={1,2,3,4,7,8,9,12}
dict2={1,2,3,0,14,12}
print(dict1.intersection(dict2))

OUTPUT:
  {1, 2, 3, 12}
  

  
