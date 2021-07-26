import sys
import Constants as C
import BasicModules as B
import TrigBody as T
sys.setrecursionlimit(20000)

def sin(x, n):
    x = x%360
    if x%90 == 0:
        if (x//90)%2 == 1:
            if ((x//90)//2)%2 == 1:
                return -1
            else: 
                return 1
        else:
            return 0
    else:
        pi2deg = C.pi2(29)/180
        if n == 0:
            return T.f(x*pi2deg, n)
        else:
            return T.f(x*pi2deg, n) + sin(x,n-1)

def cos(x, n):
    x = x%360
    if x%90 == 0:
        if (x//90)%2 == 1:
            return 0
        else:
            if x%360 == 0:
                return 1
            else:
                return -1
    else:
        pi2deg = C.pi2(29)/180
        if n == 0:
            return T.g(x*pi2deg, n)
        else:
            return T.g(x*pi2deg, n) + cos(x,n-1)

def tan(x, n):
    return sin(x, n)/cos(x, n)#maximum limit n = 84
