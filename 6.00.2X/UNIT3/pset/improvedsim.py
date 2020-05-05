import time
from ps3b import Patient, SimpleVirus, simulationWithoutDrug
import pylab as plt


def simulationWithoutDrug2(numViruses, maxPop, maxBirthProb, clearProb,
                           numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    # var for updates/timeticks
    totupdates = 300
    # list for average size
    avgsize = [0]*totupdates
    # for numTrials perform:
    for Trial in range(numTrials):
        # initiate viruses for patient
        viruses = [SimpleVirus(maxBirthProb, clearProb)
                   for v in range(numViruses)]
        # initiate patient
        testsubject = Patient(viruses, maxPop)
        # simulate 300 changes to viruspop i.e. 300x update
        for step in range(totupdates):
            # update and ad value to list
            toAdd = testsubject.update()
            avgsize[step] += toAdd
    # calc average of trials per timeste for every update: data/numTrials
    for datapoint in range(totupdates):
        avgsize[datapoint] = avgsize[datapoint]/numTrials

    # plot average size of the virus pop as func of time
    fig, ax = plt.subplots()
    ax.plot(avgsize)
    ax.set(xlabel='time', ylabel='Avg. Viruses',
           title='Average viruses in body at each timestep')
    # plt.show()


for i in [1, 5, 10, 100, 200]:
    print("Current:{}".format(i))
    start = time.time()
    simulationWithoutDrug(10, 50, 0.1, 0.05, i)
    print("Ende alt: {}".format(time.time()-start))
    start = time.time()
    simulationWithoutDrug2(10, 50, 0.1, 0.05, i)
    print("Ende neu: {}".format(time.time()-start))
    time.sleep(2)
time.sleep(5)
