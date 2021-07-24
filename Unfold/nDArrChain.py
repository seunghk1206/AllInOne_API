import sys
sys.setrecursionlimit(200000)
import UnfoldBodies as UFB
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

def arrDivArr(arr1D, indArr):
    if sorted(nDUnf(indArr)) == [each for each in range(len(arr1D))]:
        return UFB.passArrDiv(arr1D, indArr)
    else:
        try:
            Ex = IndexError()
            Ex.sterror = "The index array does not match the length of input array! The length of your array is " + str(len(arr1D)) + " where as it is " + str(len(nDUnf(indArr))) + " for the ind array"
            raise Ex
        except IndexError as E:
            print("Not full index array error!", E.sterror)

def nDarr2IndArr(nDarr):
    return UFB.nDarr2IndArrBod(nDarr, [i for i in range(len(nDUnf(nDarr)))])

print(arrDivArr([101, 400, 600, 300, 222, 100], [[[[[[[[0]]]]]], 3, [2, 4], 5]]))