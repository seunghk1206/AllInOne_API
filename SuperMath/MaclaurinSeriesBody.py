import BasicModules as B

def summateExponent(x, precision):
    if precision == 0:
        return 1
    else:
        return x**precision/B.factorial(precision)+summateExponent(x, precision-1)

def summateFractional(x, precision):
    if precision == 0:
        return 1
    else:
        return x**precision + summateFractional(x, precision-1)