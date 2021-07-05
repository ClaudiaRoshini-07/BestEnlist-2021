//1.	Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.

la = [1, 3, 5, 7]
lb = [2, 4, 6, 8]
list(zip(la, lb))

OUTPUT:
[(1, 2), (3, 4), (5, 6), (7, 8)]

//2.	First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.

lst1=["Energy", "Anne", "Irene", "Tina", "Fern", "Finch", "Tin"]
rng1 = list(range(1,8))
lst = zip(lst1, rng1)
print(lst)

OUTPUT:
[('Elna', 1), ('Anne', 2), ('Irene', 3), ('Tina', 4), ('Fern', 5), ('Finch', 6), ('Tin', 7)]

//3.	Using sorted() function, sort the list in ascending order.

x = (1, 9, 4,8,2,6,3)
y = sorted(x)
print(y)

OUTPUT:
[1, 2, 3, 4, 6, 8, 9]

//4.	Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.

x = [1,2,3,4,5,6,7,8,9,10,13,15]
def odd_num(num):
    if(num%2 != 0):
        return True
    else:
        return False

oddNums = filter(odd_num, x)
print('odd Numbers:')
a =[]
for num in oddNums:
    a.append(num)
print(a)

OUTPUT:
odd Numbers:
[1, 3, 5, 7, 9, 13, 15]
