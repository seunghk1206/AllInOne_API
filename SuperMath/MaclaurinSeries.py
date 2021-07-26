import BasicModules as B
import MaclaurinSeriesBody as MB

def exponentMaclaurin(x, precision):
    return MB.summateExponent(x, precision) #precision -> inf more precise the value is

def fractional(x, precision): # return 1/(1-x) in maclaurin series for |x| < 1
    return MB.summateFractional(x, precision) # when x = 1, undefined