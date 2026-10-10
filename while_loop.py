# print number 1 to 5
i=1
while i<=5:
    print(i)
    i+=1

# print number 5 to 1
i=5
while i>=1:
    print(i)
    i-=1

#print the multiplication table of a number n
n=5
i=1
while i<=10:
    print(n*i)
    i+=1

#print the factorial (12!)
n=12
fact=1
while n>0:
    fact= fact*n
    n=n-1
    print(fact)

#print even number 1 to 20
i=2
while i<=20:
    print(i)
    i+=2


#print odd number 1 to 20
i=1
while i<=20:
    print(i)
    i+=2


# sum of numbers 1 to 10
i=1
sum=0
while i<=10:
    sum=sum+i
    print(sum)
    i+=1

# sum of even numbers
i=2
sum=0
while i<=20:
    sum=sum+i
    print(sum)
    i+=2

# print 1 to 100 cube
i=1
while i<=100:
    print(i,"cube",i**3)
    i+=1

# print 1 to 100 square
i=1
while i<=100:
    print(i,"square",i**2)
    i+=1

# square pattern
* * * * *                
* * * * *
* * * * * 
* * * * * 
i=1
while i<=4:
    j=1
    while j<=4:
        print("*",end = " ")
        j+=1
    print ()
    i+=1

# increasing traingel
*
* * 
* * * 
* * * * 
* * * * * 
i=1
while i<=5:
    j=1
    while j<=i:
        print("*", end = " " )
        j+=1
    print()
    i+=1


# Decreasing traingel 
* * * * * 
* * * * 
* * * 
* * 
* 
i=5
while i>=1:
    j=1
    while j<=i:
        print("*", end = " " )
        j+=1
    print()
    i-=1

# number traingel 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 

i=1
while i<=5:
    j=1
    while j<=i:
        print (j , end = " " )
        j+=1
    print()
    i+=1

# same numbere traingel
1
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 

i=1
while i<=5:
    j=1
    while j<=i:
        print (i, end = " " )
        j+=1
    print()
    i+=1

#print number using break
i=1 
while i<=20:
    print(i)
    if i==10:
        break
    i+=1


#print number using continue 
i=0
while i<5:
    i+=1
    if i==3:
        continue 
    print(i)

#print number using the pass 
i=0
while i<5:
    i+=1
    if i==3:
        continue 
    print(i)

#print number using pass 
i=0
while i<5:
    if i==3:
        pass
    i+=1
    print(i)




























































