#To get sorted list
l1=[2,55,7,1,63,25,100,87,5,11]
print(l1)
print('\n')
l1.sort()
print(l1)
l1.reverse()
print(l1)
l1.append(45) #adds 45 at the end of the list
print(l1)
l1.insert(2, 544) #insert 544 in the 2nd position
print(l1)
l1.pop(2) #remove the element at the 2nd index
print(l1)
l1.remove(25) #remove 25 from the list
print(l1)


***OUTPUT***

[2, 55, 7, 1, 63, 25, 100, 87, 5, 11]


[1, 2, 5, 7, 11, 25, 55, 63, 87, 100]
[100, 87, 63, 55, 25, 11, 7, 5, 2, 1]
[2, 55, 7, 1, 63, 25, 100, 87, 5, 11, 45]
[2, 55, 544, 7, 1, 63, 25, 100, 87, 5, 11]
[2, 55, 1, 63, 25, 100, 87, 5, 11]
[2, 55, 7, 1, 63, 100, 87, 5, 11]
> 
