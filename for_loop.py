# print number 1 to 10
for i in range (1,11):
    print(i)

# print number 10 to 1
for i in range (10,0,-1):
    print(i)

# print even number
for i in range (2,21,2):
    print(i)
    
# print 0dd number
for i in range (1,20,2):
    print(i)

# Tabel print
n= int(input("enter a number:"))
for i in range(1,11):
    print(n*i)

#multiplication table 1 to 3
for n in range (1,4):
    for i in range (1,11):
        print (n*i)

# print factorial of a number       
n=5
fact=1
for i in range (1,n+1):
    fact=fact*i
    print(fact)

# print square 
for i in range (1,6):
    print (i,"=",i*i)

# print cube 
for i in range (1,6):
    print (i,"=",i**3)


# string based
name ="python"
for ch in name:
    print(ch)

# square star pattern
for i in range (1,4):
    for j in range (1,4):
        print("*", end= " " )
    print()

# Right traingel 
for i in range (1,4):
    for j in range (i):
        print("*", end= " " )
    print()

# Invertted traingel 
for i in range (5,0,-1):
    for j in range (i):
        print("*", end= " " )
    print()

# same number pattern 
for i in range (1,6):
    for j in range (i):
        print(i,end = " ")
    print()

# Different number pattern 
for i in range (1,6):
    for j in range (1,i+1):
        print(j,end = " ")
    print()



    



















    



























