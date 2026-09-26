#create a dictionary contaning a student name ,age,and markes
student={"name":"priya",
"age":23,
"marks":56}
print(student)

#print all keys
print(student.keys())

print all values
print(student.values())

#add  a new key value pair
student["city"]="indore"
print(student)
student["name"]="antim"
print(student)

#delete a key value pair
del student["name"]
print(student)             

#check wheather a key exist
#if "age" is student:
    print("key exists")
else:
   print("key does not exist")

#count the number of item
print(len(student))  

#create a nested dictionary of multipel student 
students={
    "student1":{"name":"priya","marks":67},
    "student2":{"name":"antim","marks":70}
    }
print(students)