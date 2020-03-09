def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup. 
    '''
    oddTuple = ()
    for n in range(0, len(aTup), 2):
        oddTuple += (aTup[n],)
    return oddTuple


print(oddTuples((1, 2, 3, 4, 5, 6, 7, 8, 9)))
