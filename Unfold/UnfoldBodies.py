def nDarr2IndArrBod(nDarr, currIndL):
    retL = []
    inpIndL = currIndL
    for each in nDarr:
        if type(each) == list:
            retL.append(nDarr2IndArrBod(each, inpIndL))
        else:
            retL.append(inpIndL[0])
            inpIndL.remove(inpIndL[0])
    return retL

def passArrDiv(arr1D, indArr):
    retL = []
    for each in range(len(indArr)):
        if type(indArr[each]) == list:
            retL.append(passArrDiv(arr1D, indArr[each]))
        else:
            retL.append(arr1D[indArr[each]])
    return retL