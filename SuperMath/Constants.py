import BasicModules as B
import Trig as T
def eulerNumber(precision):
    if precision != 0:
        return 1/B.factorial(precision)+eulerNumber(precision-1)#20 is the limit threshold. It makes no difference in limit is larger than 20
    else:
        return 1

def eulerNumber2(precision):
    return (1+precision)**(1/precision) #precision -> 0, more precise the e is

def eulerNumber3(precision):
    return (1+1/precision)**(precision) #precision -> inf, more precise the e is

def piF(x):
    return B.factorial(4*x)/(B.factorial(x))**4*(26390*x+1103)/396**(4*x)

def summatePiF(limit):
    if limit == 0:
        return piF(limit)
    return piF(limit) + summatePiF(limit-1)

def pi(precision):
    return 1/2*precision*T.sin(360/precision, 84) #precision -> inf, more precise the pi is

def pi2(precision):
    return 99**2/(2*(2)**(1/2))*1/summatePiF(precision) #precision -> inf, more precise the pi is.