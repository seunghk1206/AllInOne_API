import Trig as T

def EulerRule(x, n):
    return str(T.cos(x, n))+'+'+'i'+'*'+str(T.sin(x, n))
