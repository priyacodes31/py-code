#create a tuptl contaning 5 numbers.
t=(4,7,8,9,10)
print(t)
#length
print(len(t))

#find the maximum and minimum numbers
print("maximum:",max(t))
print("minimum:",min(t))

#count how many types an elements occurs.
print (t.count (8))

#find the index of an element 
print(t.index(10))
#convert to list into tuple
l=[10,20,30,40,50]
t= tuple(l)
print(t)

#convert a tupel in to a list
T=("apple","mango","Orange")
l= list(T)
print(l)

#create a nested tupel and access its element
numbers=((1,2),(3,4),(5,6))
print(numbers[0])