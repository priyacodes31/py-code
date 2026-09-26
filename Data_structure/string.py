#string ordered,immutabel
#Take a string as input and print it.
first_name=input("enter a first name:")
last_name=input ("enter a last name:")
full_name=first_name +"  " + last_name
print(full_name)

#find the length of a string
print(len(full_name))

#convert to string to upper case and lower case
print(full_name.upper())
print(full_name.lower())

#check whether string is a palindrome.
list1=["121", "madam","121"]
copy_list1= list1.copy()
copy_list1.reverse()
if list1==copy_list1:
    print("list is palindrome")
else:
    print("not palindrome")

#check wheather a string starts or ends with a particular word  
text="python programming"
print(text.startswith("py"))
print(text.endswith("ng"))

print(text[::-1]) #reverse string

#count how many times a particular character appears.
fruits="banana"
print(fruits.count("a"))

#replaces a word in a string with another word.
text="i love java"
print(text.replace("java","python")) 