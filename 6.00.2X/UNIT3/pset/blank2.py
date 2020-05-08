from ps3b_precompiled_37 import *
import pylab


def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)

    """
    halfticks = 150
    avgpop = [0]*(halfticks*2)
    respop = [0]*(halfticks*2)
    # performe num trials
    for Trial in range(numTrials):
        # init viruses
        viruses = [ResistantVirus(maxBirthProb, clearProb, resistances,
                                  mutProb) for v in range(numViruses)]
        # init patient
        testsubject = TreatedPatient(viruses, maxPop)
        # simulate 150 changes without treatment:
        for step in range(halfticks*2):
            # update and ad val to list:
            toadd = testsubject.update()
            avgpop[step] += toadd
            respop[step] += testsubject.getResistPop(list(resistances.keys()))
    # calc average
    for datapoint in range(len(avgpop)):
        avgpop[datapoint] = avgpop[datapoint]/numTrials
    # for resistant
    for datapoint in range(len(respop)):
        respop[datapoint] = respop[datapoint]/numTrials

    pylab.plot(avgpop, label="SimpleVirus")
    pylab.plot(respop, label="Resistant Virus")
    pylab.title("SimpleVirus simulation")
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.legend(loc="best")
    pylab.show()


simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005)
