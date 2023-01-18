a={1,2,4,6,23,9,1,2,4,1,9,23,6}
print(type(a))
print(a) #won't repeat the elements
b={} #IMPORTANT:This syntax will create an empty dictionary and not an empty set.
print(type(b))
#An empty set can be created using the following syntax
c=set()
print(type(c))
#Adding values to an empty set
c.add(4)
c.add(5)
c.add(5) #5 won't be added multiple times.Adding a value repeatedly does not change the set
print(c)
c.add((6,4,5)) #Can add tuple but cam't add list. Also can't add dictionary
print(c)
print(len(c)) #Prints the length of the set
c.remove(5) #Removes 5 from the setif it is present
print(c)
#b.remove(95) will throw an error as 95 is not in the set
print(c.pop()) #Removes an element from the set randomly and returns it
print(c)

***OUTPUT***

<class 'set'>
{1, 2, 4, 6, 23, 9}
<class 'dict'> #Shows dictionary
<class 'set'>
{4, 5}
{(6, 4, 5), 4, 5}
3
{(6, 4, 5), 4}
(6, 4, 5)
{4}
> 
