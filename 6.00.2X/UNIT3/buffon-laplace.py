import random
import math
import statistics


def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1, numNeedles+1):
        x = random.random()
        y = random.random()
        if (x*x+y*y)**0.5 <= 1.0:
            inCircle += 1
    sol = 4*(inCircle/(float(numNeedles)))
    return sol


def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = statistics.stdev(estimates)
    curEst = sum(estimates)/len(estimates)
    print(
        f"Est.= {curEst},\n Std. dev. = {round(sDev,4)},\n Needles = {numNeedles}")
    return (curEst, sDev)


def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/2:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst


print(estPi(0.01, 100))
