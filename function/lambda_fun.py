#lambda function
#print square
square=lambda a:a**2
print(square(5))

#add two number
add=lambda a,b:a+b
print(add(12,12))

#find cube
cube=lambda a:a**3
print(cube(12))

#check even or odd 
check=lambda n:"even" if n%2==0 else"odd"
print(check(113))

#find the largest of two number 
largest =lambda a,b:a if a>b else b
print(largest(23,45))

#find the length of a string
length=lambda text:len(text)
print(length("python programming"))

#convert celsius to fahrehnit
convert=lambda c:(c*9/5)+32
print(convert(30))



