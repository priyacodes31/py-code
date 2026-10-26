# level 1
# write a function to print Hello world.
def greet ():
    print("Hello world!")
greet()

#write a function to add two number
def add(a,b):
    print(a+b)
add(12,12)

#write a function to square of a number
def square (a):
    return a*a
print(square(5))

# write a function to cube of a number 
def cube(n):
    return n*n
print(cube(45))

# write a function to check whether a number is even or odd 
def check_even (n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print (check_even(5))


#write a function two find a maximum of two number 
def maximum (a,b):
    print(max(a,b))
maximum(10,99)

#write a function two find a minimum of two number 
def minimum(a,b):
    if a<b:
        return a
    else:
        return b
print(minimum(90,44))

#write a function two find average of a numbers.
def average (x,y,z):
    return x+y+z/3
print(average(90,56,78))

#write a program to convert celcius to faherenhit.
def celcius_feh(c):
    f=(c*9/5)+32
    print(f)
celcius_feh(100)
celcius_feh(0)

#Intermidate function programs.
#LEVEL 2
#write a program to find factorial of a number n
def factorial(n):
    result=1
    for i in range (1,n+1):
        result*=i
    return result
print(factorial(5))

# write a fuction to retuen largest number in a list 
def lar_no_list(my_list):
    return max(my_list)
print (lar_no_list([12,89,90,99,34,6]))

# write a function a reverse a string
def reverse_string(s):
    return s[::-1]
print(reverse_string("python programming"))

#find sum of list element 
def sum_list(numbers):
    total=0
    for n in numbers :
        total+=n
        print(total)
sum_list([10,30,20 ])

#multiplication table
def multiplication(n):
    for i in range (1,11):
        print(n,"*",i ,"=",n*i)
multiplication (4)
    
#write a function to count character in string 
def count_char(text):
    print(len(text))  
count_char("priyanka patidar")   

#palindrome 
def reverse_string(s):
    return s[::-1]

def is_palindoreme(s):
    s=s.lower 
    return s==reverse_string(s)
print(is_palindoreme("naman"))