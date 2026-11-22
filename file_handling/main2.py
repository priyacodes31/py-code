#reading a csv file 
#import csv
#with open("student.csv","r") as file:
 #   reader= csv.reader(file)
  #  for row in reader:
   #      print(row)


#writing a csv file     
#import csv 
#with open("student.csv","w")as file:
 #   writer=csv.writer(file)
  #  writer.writerow(["name","age","marks"])
   # writer.writerow(["priya","23","97"])

#write a json file
import json
student={"name":"ruhi",
"age":23,
"marks": 90}
with open ("student.json","w") as file:
    json.dump(student,file)

#reading a json file 
import json
with open("student.json","r") as file:
   data= json.load(file)
   print(data)
   print(data["name"])
   print(data["marks"])