from VDC import VersatileDeciConverter as VDC
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
def nDArr2nNom(arr, nNom):
    retL = []
    unfL = nDUnf(arr)
    for each in unfL:
        retL.append(VDC.versatileDeci(0, each, nNom))
    return retL

print(nDUnf([20, [1,2,3,1,2], [1,2,0,0,0], [1,1,2], [[3], [1,5,2]]]))