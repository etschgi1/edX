import numpy as np
import os
c = [1, 2, 2, 3]

t = 4
os.environ["OPENBLAS_NUM_THREADS"] = "1"


def generateAllBinaryStrings(n, arr, i):

    if i == n:
        for i in range(0, n):
            print(arr[i], end=" ")
        addtolist(arr, n)
        return

    # First assign "0" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1)

    # And then assign "1" at ith position
    # and try for all other permutations
    # for remaining positions
    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1)


def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    # all 0,1 combinations
    l = len(choices)
    arr = [None]*l
    print(generateAllBinaryStrings(l, arr, 0))


find_combination(c, t)
