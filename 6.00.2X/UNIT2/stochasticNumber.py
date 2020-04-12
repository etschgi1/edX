import random


def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number 
    between 9 and 21
    '''
    i = random.randint(9, 21)
    return i if i % 2 == 0 else stochasticNumber()
