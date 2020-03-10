animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(aDict):
    length = map(len, aDict.values())
    length = list(length)  # creates a list from the map using len on dict val
    for key, val in aDict.items():  # walks through each key val pair in dict
        if len(val) == max(length):  # checks which val is of max length and
            return key  # returns its key
    return 'Key does not exist'


print(biggest(animals))
