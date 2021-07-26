import BasicModules as B

def f(x, n):
    return (((-1)**n)*x**(2*n+1)/B.factorial(2*n+1))

def g(x, n):
    return (((-1)**n)*x**(2*n)/B.factorial(2*n))