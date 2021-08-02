# =================MaclauringSeries===============
import MaclaurinSeries as M
import MaclaurinSeriesBody as MB


def exponentMaclaurin(x, precision):
    return M.exponentMaclaurin(x, precision)

def summateFractional(x, precision):
    return MB.summateFractional(x, precision)

def fractional(x, precision): # return 1/(1-x) in maclaurin series for |x| < 1
    return summateFractional(x, precision) # when x = 1, undefined

# ==================Constant====================
import Constants as C

def eulerNumber(precision):
    return C.eulerNumber(precision)

def eulerNumber2(precision):
    return C.eulerNumber2(precision)

def eulerNumber3(precision):
    return C.eulerNumber3(precision)

def piF(x):
    return C.piF(x)

def summatePiF(limit):
    return C.summatePiF(limit)

def pi(precision):
    return C.pi(precision)

def pi2(precision):
    return C.pi2(precision)

# ==================Trig======================
import Trig as T

def sinMod(x, n):
    return T.sin(x, n)

def sin(x):
    return sinMod(x, 84)

def cosMod(x, n):
    return T.cos(x, n)

def cos(x):
    return cosMod(x, 84)

def tanMod(x, n):
    return sinMod(x, n)/cosMod(x, n)#maximum limit n = 84

def tan(x):
    return tanMod(x, 84)

# ==================EulerRule======================
import EulerCalc as E

def EulerRuleMod(x, n):
    return E.EulerRule(x, n)

def EulerRule(x):
    return EulerRuleMod(x, 84)
