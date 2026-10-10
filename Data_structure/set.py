#create a set of numbers
s={10,40,67,89,50,80}
print(s)
#add an elements to a set
s.add(70)
print(s)

#remove an elements from a set
s.remove(40)
print(s)

#find the union of two sets
a= {10,20,30,40}
b={30,40,50,60}
print(a.union(b))

#find the intersection of two sets
a={1,2,3,4}
b={3,4,5,6}
print(a.intersection(b))

#find the diff betwwn two sets
a={10,20,30,40}
b={40,50,60,70}
print(a.difference (b))

#find the symmetric diff 
print(a.symmetric_difference(b))

#remove a duplicate value list using a set
numbers=[70,60,50,10,50,60,70,20,10]
new=list(set(numbers))
print(new)