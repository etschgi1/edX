import random
import pylab as plt
import statistics as stat


def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3
    balls of the same color were drawn.
    '''
    success = 0
    for Trail in range(numTrials):
        balls = ['g', 'g', 'g', 'r', 'r', 'r']
        drawn = []
        for _ in range(3):  # 3 times drawn
            draw = random.choice(balls)
            drawn.append(balls.pop(balls.index(draw)))
        if drawn[0] == drawn[1] and drawn[1] == drawn[2]:
            success += 1
    return success/numTrials


def runsim(Trails, numTrials):
    '''Runs the noReplacementSimulation Trails times with numTrials
    Returns the st dev '''
    results = []
    for Trail in range(Trails):
        print(Trail)
        results.append(noReplacementSimulation(numTrials))
    stddev = stat.stdev(results)
    mean = stat.mean(results)
    return results, stddev, mean


Trials = 200
numTrials = 5000
bins = 20
r, rd, rm = runsim(Trials, numTrials)
r2, rd2, rm2 = runsim(Trials, numTrials)
with plt.xkcd():
    fig, axes = plt.subplots(1, 2)
    plt.suptitle("Number 3 of same color are drawn for\n "
                 "{} tests with {} runs each.".format(Trials, numTrials))
    axes[0].hist(r, color="y", density=True, bins=bins)
    axes[1].hist(r2, color="r", density=True, bins=bins)
    for ax in axes:
        ax.set(xlabel='Probability of 3 of same color',
               ylabel='pdf for {} trials'.format(Trials))
    # plt.tight_layout()
    fig.set_size_inches(10, 8)  # Size of the plot
print(rd, "  ", rd2, " \nmean: ", rm, "  ", rm2,)
plt.show()
