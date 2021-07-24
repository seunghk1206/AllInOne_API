# ==================Trig======================
import Trig as T

def factorial(x):
    return T.factorial(x)

def eulerNumber(precision):
    return T.eulerNumber(precision)

def eulerNumber2(precision):
    return T.eulerNumber2(precision)

def eulerNumber3(precision):
    return T.eulerNumber3(precision)

def piF(x):
    return T.piF(x)

def summatePiF(limit):
    return T.summatePiF(limit)

def pi(precision):
    return T.pi(precision)

def pi2(precision):
    return T.pi2(precision)

def summateExponent(x, precision):
    return T.summateExponent(x, precision)

def exponentMaclaurin(x, precision):
    return T.exponentMaclaurin(x, precision)

def summateFractional(x, precision):
    return T.summateFractional(x, precision)

def fractional(x, precision): # return 1/(1-x) in maclaurin series for |x| < 1
    return summateFractional(x, precision) # when x = 1, undefined

def f(x, n):
    return T.f(x, n)

def sinMod(x, n):
    return T.sin(x, n)

def sin(x):
    return sinMod(x, 84)

def g(x, n):
    return T.g(x, n)

def cosMod(x, n):
    return T.cos(x, n)

def cos(x):
    return cosMod(x, 84)

def tan(x, n):
    return sin(x, n)/cos(x, n)#maximum limit n = 84

# ==================EulerRule======================
import EulerCalc as E

def EulerRuleMod(x, n):
    return E.EulerRule(x, n)

def EulerRule(x):
    return EulerRuleMod(x, 84)
