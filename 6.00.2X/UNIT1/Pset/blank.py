cow = {'Maggie': 3, 'Herman': 7, 'Betsy': 9, 'Oreo': 6, 'Moo Moo': 3,
       'Milkshake': 2, 'Millie': 5, 'Lola': 2, 'Florence': 2, 'Henrietta': 9}
test = {'Maggie': 3, 'Herman': 6, 'Betsy': 2, 'Oreo': 4}
test2 = {'Horns': 50, 'Miss Bella': 15, 'Muscles': 65, 'Milkshake': 75,
         'Louis': 45, 'Patches': 60, 'Lotus': 10, 'Clover': 5, 'MooMoo': 85, 'Polaris': 20}
# test2 with 100


def greedy_cow_transport(cows, limit=10):
    '''cows dict with name and weight, limit max that ship can carry
    returns list of lists with inner lists being seperate trip
    '''
    solution = []
    tempcow = cows.copy()
    while True:
        if len(tempcow) == 0:
            return solution
        tempsol = []
        available = limit
        print('tempsol reset')
        while True:  # single Trips
            if len(tempcow) == 0:
                break
            totake = fatcow(tempcow, available)
            print(totake)
            if tempcow[totake] <= available:
                available -= tempcow[totake]
                print(totake)
                tempsol.append(totake)  # add cow to solution
                del tempcow[totake]
                print('end if')

            else:
                print("break")
                break
        solution.append(tempsol)
        print("-------------")


def fatcow(cows, maximum):
    '''returns fattest cow for weight'''
    weight = 0
    name = ''
    for cow in cows:
        if cows[cow] > weight and cows[cow] <= maximum:
            name = cow
    return name

    # if cows:
    # weight = 0
    # for cow in cows:
    #     name = cow
    #     if cows[cow] >= weight and cows[cow] <= maximum:
    #         weight = cows[cow]
    # fatcow = [name, cows[name]]
    # return fatcow


print(greedy_cow_transport(test2, 100))
# greedy_cow_transport(cow)
