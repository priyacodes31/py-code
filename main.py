#reading a file 
#file=open("demo.text","r")
#data=file.read()
#print(data)
#file.close()

#if you open a non existing file in a read mode.
#file=open("abc.txt","r")
#data=file.read()
#print(data)
#file.close()

##reading a one line
#file=open("demo.text","r")
#line1=file.readline()
#print(line1)
#file.close()

#read all lines 
file=open("demo.text","w")
file.write("python\n java\n c++")
file.close()

file=open("demo.text","r")
data=file.readlines()
print(data)
file.close()

# write data in to a file
file=open("demo.text","w")
file.write("nurturing the young Mind")
file.close()

file=open("demo.text","r")
data=file.read()
print(data)
file.close()

#append data in to a file
file=open("demo.text","a")
file.write("\n Reflections on the year of AI")
file.close()

file=open("demo.text","r")
result=file.read()
print(result)
file.close()

#count character in a file
file=open("demo.text","w")
file.write("the life of a teacher/n CYBER SAFETY TIPS/nSTRONG PASSWORDS /nSMART SHARING")
file.close()

file=open("demo.text","r")
result=file.read()
print("Total character in a file:",len(result))
file.close()

#count words in a file 
file=open("demo.text","w")
file.write("the life of a teacher/n CYBER SAFETY TIPS/nSTRONG PASSWORDS /nSMART SHARING")
file.close()

file=open("demo.text","r")
data=file.read()
words=data.split()
print("Total words",len(words))
file.close()

# search a word in a file 
file=open("demo.text","w")
file.write("the life of a teacher/n CYBER SAFETY TIPS/nSTRONG PASSWORDS /nSMART SHARING")
file.close()

file=open("demo.text","r")
data=file.read()
word="life"
if word in data:
    print("word exist")
else:
    ("word not exist ")
file.close()

#convert text in to uppercase 
file=open("demo.text","w")
file.write("the life of a teacher")
file.close()

file=open("demo.text","r")
data=file.read()
print(data)
file.close()

file=open("demo.text","w")
file.write(data.upper())
file.close
print("text converted in to a uppercase")

file=open("demo.text","r")
data=file.read()
print(data)
file.close()

#check whether a file exists 
import os
if os.path.exists("demo.text"):
    print("file exists")
else:
    print("file does not exists")

#Delete a file
import os
if os.path.exists("demo.text"):
    os.remove("demo.text")
    print("file deleted succesfully")
else:
    print("file not found")

#create a file write mode 
file=open("demo.text","w")
file.write("PM SHRI JNV AGAR MALWA")
file.close()

file=open("demo.text","r")
data=file.read()
print(data)
file.close()








