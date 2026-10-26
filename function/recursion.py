#print number from 1 to N
def numbers(n):
    if n==0:
        return
    numbers(n-1)
    print(n)
numbers(100)

#print numbers from N to 1
def numbers (n):
    if n==0:
        return
    print(n)
    numbers(n-1)
numbers(100)

#power of a number 
def power(a,n):
    if n==0:
        return 1
    return a*power(a,n-1)
print(power(5,5))

#factorial of a number 
def fact(n):
    if n==0:
        return 1
    return n *fact(n-1)
print(fact(5))

#sum of digit 
def sum_digit(n):
    if n==0:
        return 0
    return(n%10)+sum_digit(n//10)
print(sum_digit(45678))

#count digit in a number 
def count_digit(n):
    if n<10:
        return 1
    return 1+count_digit(n//10)
print(count_digit(19880000000))

#fibonacci series 
def fibonacci (n):
    if n<=1:
        return n
    return(fibonacci(n-1)+fibonacci(n-2))
print(fibonacci(6))


#print hello 5 times 
def hello (n):
    if n==0:
        return
    print("hello")
    hello(n-1)
hello(5)