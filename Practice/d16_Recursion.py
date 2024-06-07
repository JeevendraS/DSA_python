def SumN(n):
    if n<=1:
        return 1
    print(n)
    return n + SumN(n-1)

def factorialN(n):
    if n==1:
        return 1
    return n * factorialN(n-1)
def firstN(n):
    if n>0:
        firstN(n-1)
        print(n)
def firstNR(n):
    if n>0:
        print(n)
        firstNR(n-1)
def firstNodd(n):
    if n>0:
        firstNodd(n-1)
        print((2*n)-1)
def firstNeven(n):
    if n>0:
        firstNeven(n-1)
        print((2*n)-2)

def firstNsum(n):
    if n==1:
        return 1
    return n + firstNsum(n-1) 

def SumOfsquare(n):
    if n>1:
        print(n*n)
        return (n*n) + SumOfsquare(n-1)
    return 1







print(SumOfsquare(5))