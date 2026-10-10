#create a list and print it.
numbers=[10,20,30,40,50]
print(numbers)

#find the length of list 
print(len(numbers))

#find thelargest and smallest number in a list.
print("largest number",max(numbers))
print("smallest number",min(numbers))

#calculate the sum of all number in a list.
print(sum(numbers))

#add an element to a list.
numbers.append(60)
print(numbers)

#remove an item from a list
numbers.remove(40)
print(numbers)
#reverse a list
numbers.reverse()
print(numbers)
 
 #remove duplicates value from a list
list=[1,2,7,3,2,8,7,2,8]
new_list=set(list)
print(new_list)