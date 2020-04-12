from walksetup import *


def walk(f, d, numSteps):
    """
    Assumes: f a Field, d a Drunk in f, and numSteps an int >=0
    Moves d numSteps times; returns the distance between the final location
    and the location at the start of the walk.
    """
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))


def simWalks(numSteps, numTrials, dClass):
    """[Simulates numTrials walks of numSteps steps each]

    Arguments:
        numSteps {[int]} -- [>=0]
        numTrials {[int]} -- [>0]
        dClass {[str]} -- [to simulate for different 
        drunk subclasses]
    """
    Homer = dClass('homer')
    origin = Location(0, 0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances


def drunkTest(walkLenghts, numTrials, dClass):
    """[For each number of steps in walkLenghs runs simWalks
     and prints results]

    Arguments:
        walkLenghts {[int]} -- [sequence of ints > 0]
        numTrials {[int]} -- [number of trials for simwalk >0]
        dClass {[str]} -- [type of drunk to use in simulation]
    """
    for numSteps in walkLenghts:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, ' random walk of ', numSteps, ' steps')
        print('Mean = ', round(sum(distances)/len(distances), 4))
        print('Max = ', max(distances), 'Min = ', min(distances))


random.seed(0)
drunkTest([1000, 10000, 100000], 10, UsualDrunk)
print("------------------------")
drunkTest([1000, 10000, 100000], 10, ColdDrunk)
