import random


def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    i = random.randint(0, 99)
    return i if i % 2 == 0 else genEven()


print(genEven())
