from SuperMath import *
from SuperMath import PackageInit as SMPI
from Unfold import nDArrChain as UnDPI
from VDC import PackageInit as VDCPI
class SuperMath:
    def __init__(self, precision, Pi2precision):
        self.precision = precision
        self.Pi2precision = Pi2precision
        return None
    def summateExponent(self, x):
        return SMPI.summateExponent(x, self.precision)

    def exponentMaclaurin(self, x):
        return SMPI.exponentMaclaurin(x, self.precision)

    def summateFractional(self, x):
        return SMPI.summateFractional(x, self.precision)

    def fractional(self, x): # return 1/(1-x) in maclaurin series for |x| < 1
        return SMPI.fractional(x, self.precision) # when x = 1, undefined

    # ==================Constant====================

    def eulerNumber(self):
        return SMPI.eulerNumber(self.precision)

    def eulerNumber2(self):
        return SMPI.eulerNumber2(self.precision)

    def eulerNumber3(self):
        return SMPI.eulerNumber3(self.precision)

    def pi(self):
        return SMPI.pi(self.precision)

    def pi2(self):
        return SMPI.pi2(self.Pi2precision)

    # ==================Trig======================

    def sin(self, x):
        return SMPI.sinMod(x, self.precision)

    def cos(self, x):
        return SMPI.cosMod(x, self.precision)

    def tan(self, x):
        return SMPI.tanMod(x, self.precision)

    # ==================EulerRule======================

    def EulerRule(self, x):
        return SMPI.EulerRuleMod(x, self.precision)

Alpha = SuperMath(84, 29)