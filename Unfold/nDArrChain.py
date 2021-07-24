import sys
sys.setrecursionlimit(200000)
def nDUnf(arr):
    varL = []
    for each in arr:
        if type(each) == list:
            for EV in nDUnf(each):
                varL.append(EV)
        else:
            varL.append(each)
    return varL

def nDUnfSet(arr):
    unfolded = nDUnf(arr)
    retL = []
    for each in unfolded:
        if each in retL:
            pass
        else:
            retL.append(each)
    return retL

def div1D(arr1D, term):
    retL = [[arr1D[i*term+j] for j in range(term)] for i in range(len(arr1D)//term)]
    return retL

