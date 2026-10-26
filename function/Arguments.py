# *args programs
#print all arguments
def show (*args):
    print(args)
show(10,20,30,40,50)

#print argument one by one
def details(*args):
    for i in args:
        print(i)
details("priya",20,"indore")

# find even numbers
def even_number(*args):
    for i in args:
        if i%2==0:
            print(i)
even_number(34,67,20,44,80)


#find odd numbers
def odd_number(*args):
    for i in args:
        if i%2!=0:
            print(i)
even_number(34,89,67,55,45,56)

#calculate the average
def cal_avg(*args):
    if len (args)>0:
        print("average=",sum(args)/len(args))
    else:
        "no number provided"
cal_avg(10,20,30,40,50)

#multiply all number 
def multi(*args):
    result=1
    for i in args:
        result*=i
        print("product=",result)
multi(2,3,4)

#find the square of each number 
def square (*args):
    for i in args:
        print(i**2)
square(25,12,13,15)

#find the cube of each number
def cube(*args):
    for i in args:
        print(i**3)
cube(3,8,12,7)

#sort number in ascending order 
def sort_number(*args):
    print(sorted(args))
sort_number(90,99,45,8)

#sort number in decending order 
def sort_number(*args):
    print(sorted(args,reverse=True))
sort_number(10,20,30,40,50,60)

#find the factorial of each number 
def fact (*args):
    for n in args:
        fact=1
        for i in range (1,n+1):
            fact*=i
            print(fact)
fact(5,6)

#concatenate string
def join_words(*args):
    print(" ".join(args))
join_words("python","is","easy","to","learn")

#pass no argument 
def show(*args):
    print(args)
    print("count=",len(args))
show()



#**kwargs 

#print all keyword argument 
def details(**kwargs):
    print(kwargs)
print(details(name="priya",age=20,city="indore"))

#calculate the sum of all values 
def total(**kwargs):
     result=sum(kwargs.values())
     print("sum=",result)
total(a=20,b=30,c=40)

#find the maximum values 
def max_value(**kwargs):
    print(max(kwargs.values()))
max_value(a=45,b=67,c=89,d=34)


#find the minimum values 
def min_value(**kwargs):
    print(min(kwargs.values()))
min_value(a=45,b=67,c=89,d=34)

#count the keyword argument 
def count_arg(**kwargs):
    print("count argument=",len(kwargs))
count_arg(x=45,y=67,z=65)

#check whether a key exist
def student_det(**kwargs):
    if "name" in kwargs:
        print("name exist")
    else:
        print("name not exist")
student_det(name="sidhika",age=23,city="jaipur")

#print only keys 
def key(**kwargs):
    for key in kwargs.keys():
        print(key)
key(name="priya",age=20)


#print only value
def value (**kwargs):
    for value in kwargs.values():
        print(value)
value(name="shivani",age=23,city="ujjain")


#display student details
def student_details(**kwargs):
    for key,value in kwargs.items():
        print (f"{key}:{value}")
student_details(name="piyush",
age=45,
city="indore",
university="Davv")

#combine two dictionary 
def show_data(**kwargs):
    print(kwargs)
dict1={"name":"priyanka","age":23}
dict2={"city":"devas","course":"m.tech"}
show_data(**dict1 ,**dict2)


    