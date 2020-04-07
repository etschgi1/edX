###########################
# 6.00.2x Problem Set 1: Space Cows
from operator import itemgetter
from ps1_partition import get_partitions
import time
testcows = {'MooMoo': 50, 'Boo': 20, 'Miss Bella': 25,
            'Lotus': 40, 'Milkshake': 40, 'Horns': 25}
# ================================
# Part A: Transporting Space Cows
# ================================


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()
    try:
        f = open(filename, 'r')
    except FileNotFoundError:
        filename = "6.00.2X/UNIT1/Pset/" + filename
        f = open(filename, 'r')
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    solution = []  # stores solution
    tempcow = cows.copy()  # create temp dict for mutation
    weightlimit = limit  # set initial max weightlimit of ship
    while True:  # main loop
        tripsolution = []  # clear tripsolution
        # get a sorted list of all remaining cows
        sortedcows = getfat(tempcow, weightlimit)

        i = 0  # to increment over cows
        # for loop to get best single trip
        # check for every cow
        for cows in range(len(sortedcows)):
            # if it fits in the remaining weightlimit first cow will always be compared to shiplimit(limit)
            if sortedcows[i][1] <= weightlimit:
                # if so add cow to tripsolution
                tripsolution.append(sortedcows[i][0])
                # set new temp weightlimit of ship
                weightlimit -= sortedcows[i][1]
                # finally remove the cow from sortedcows in order to prohibit multiple occurences on same trip
                del tempcow[sortedcows[i][0]]
                # as well as multiple occurences on different trips
                del sortedcows[i]
            else:
                # if not increment 1 so that it checks next cow. Because of else
                # i will not be incremented if cow is added because next cow will then be in same place in the list
                i += 1
        # reset weightlimit to initial limit of ship
        weightlimit = limit
        # add trip to general solution
        solution.append(tripsolution)
        # if there are no cows left return the solution
        if len(tempcow) == 0:
            return solution

# Problem 1 helper function


def getfat(cows, maximum):
    '''Helper function:
        Takes in a dict of cow names and the maximum cargo limit of the ship
        Returns a sorted list of cows from fattest to lightes
    '''
    cowlist = [[name, weight] for name, weight in cows.items()]
    allowedcows = []
    for cows in range(len(cowlist)):
        cow = cowlist[cows]
        # print(cow)
        # check if cow is allowed on the ship
        if cow[1] <= maximum:
            allowedcows.append(cow)
    # sorts cows
    sortedcows = sorted(allowedcows, key=itemgetter(1), reverse=True)
    return sortedcows

# Problem 2


def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    tempcows = cows.copy()
    cownames = list(tempcows.keys())  # setup list of names to use in get_part
    possiblesol = []
    # gets partitions of
    for partition in (get_partitions(cownames)):
        alltripweight = []  # keep track of each trips weight
        # checks for every trip of a partition
        for trip in partition:
            weight = 0  # keep track of weight of each trip
            # get weight for each trip
            for cow in trip:
                cowweight = tempcows[cow]
                weight += cowweight
            alltripweight.append(weight)
        # check if trip is valid based on weight, if so add to possiblesol
        if all(weights <= limit for weights in alltripweight):
            possiblesol.append(partition)
    # gets shortest number of possible trips
    fewesttrips = min([len(partition) for partition in possiblesol])
    # returns one of best overall partitions
    for partition in possiblesol:
        if len(partition) == fewesttrips:
            return partition
    # Problem 3


def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    print("---Compare greedy_cow_transport with brut_force_cow_transport---")
    start = time.time()
    print(greedy_cow_transport(cows, limit))
    end = time.time()
    zeit = end-start
    print("Greedy took: "+str(zeit))
    start = time.time()
    print(brute_force_cow_transport(cows, limit))
    end = time.time()
    zeit = end-start
    print("Brute force took: "+str(zeit))


"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
# to call with testcows:
limit = 10
compare_cow_transport_algorithms()
