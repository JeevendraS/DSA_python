# Write a recursive function to calculate sum of first N natural numbers

def firstNsum(n):
    if n==1:
        return 1
    s = n + firstNsum(n-1)
    return s
# print(firstNsum(7))

# Write a recursive function to calculate sum of first N odd natural numbers

def firstNoddSum(n):
    if n==1:
        return 1
    s = (2*n-1) + firstNoddSum(n-1)
    return s
# print(firstNoddSum(8))

# Write a recursive function to calculate sum of first N even natural numbers

def firstNevenSum(n):
    if n>0:
        s = (2*n-2)+firstNevenSum(n-1)
        return s
    return 0
# print(firstNevenSum(8))

# Write a recursive function to calculate factorial of number

def factorial(n):
    if n==1: 
        return 1
    s = n*factorial(n-1)
    return s
# print(factorial(5))

# Write a recursive function to calculate sum of squares of first N natural numbers. 
def SumOfSquares(n):
    if n==1:
        return 1
    s = (n**2)+SumOfSquares(n-1)
    return s
print(SumOfSquares(5))


