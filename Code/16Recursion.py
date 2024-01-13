'''
Recursion: function calling itself , is called Recursion

In Recursion, problem is solved in terms of problem itself 

Each time Recursion function call to itself for little simpler versons of the original problem 
 
 '''

# Write a recursion function to calculate sum of first n natural numbers:

def sum(n):
    if n==1:
        return 1
    s = n+sum(n-1)
    return s

print(sum(6))


# factorial
def factorial(n):
    if n==1:
        return 1
    s = n*factorial(n-1)
    return s

print(factorial(15))

# recursive function for first n natural number

def firstN(n):
    if n==1:
        print(1)
        return 1
    firstN(n-1)
    print(n)

# firstN(15)  
# first natural in reverse order  
def firstNreverse(n):
    if n==1:
        print(1)
        return 1
    print(n)
    firstNreverse(n-1)

# firstNreverse(15) 

# firs n odd natural number

def firstNodd(n):
    if n==0:
        return 
    firstNodd(n-1)
    print(2*(n-1)+1)
# firstNodd(5)

# first n even natural number

def firstNeven(n):
    if n==0:
        return 
    firstNeven(n-1)
    print(2*(n-1)+2)
# firstNeven(5)

# another varient of first n natural number

def printN(n):
    if n>0:
        printN(n-1)
        print(n)
def printNreverse(n):
    if n>0:
        print(n)
        printNreverse(n-1)
def printNodd(n):
    if n>0:
        printNodd(n-1)
        print(2*n-1)
def printNoddreverse(n):
    if n>0:
        print(2*n-1)
        printNoddreverse(n-1)
printNoddreverse(5)        

