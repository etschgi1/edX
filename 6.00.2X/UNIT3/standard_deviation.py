import statistics
import math
import time
sample = ["tes", "miauh", "foooooo", "tes", "miauh", "foooooo", "tes", "miauh", "foooooo", "tes",
          "miauh", "foooooo", "tes", "miauh", "foooooo", "tes", "miauh", "foooooo", "tes", "miauh", "foooooo", ]

n = [10, 4, 12, 15, 20, 5]


def stddevOflist(s):
    """
    s: sample inputs ints or floats
    returns standard deviation
    """
    if not s:
        return math.nan
    return round(statistics.pstdev(s), 4)


print(stddevOflist(n)/(sum(n)/len(n)))


def stdDevOfLengths(s):
    """
    s: a List of sample inputs
    returns a float, the sandard deviation of the lengths of strings in list,
    NaN if L is empty.
    """
    # time.sleep(0.01)
    if not s:
        return float('nan')
    # make list of individual sample lenght
    lengths = ([len(inds) for inds in s])
    # compute mean
    mean = sum(lengths)/len(lengths)
    # compute sum of individual variance
    tot = sum([(length-mean)**2 for length in lengths])
    # compute deviation
    return (tot/len(lengths))**0.5  # standard deviation


def stdUsingMath(s):
    """s: a List of sample inputs
    returns a float, the sandard deviation of the lengths of strings in list,
    NaN if L is empty. Using math lib
    """
    # time.sleep(0.01)
    if not s:
        return math.nan
    return statistics.pstdev([len(i) for i in s])


# timelist = []
# timemat = []

# for i in range(100000):
#     start = time.time()
#     print(stdDevOfLengths(sample))
#     timelist.append(time.time()-start)
#     start = time.time()
#     print(stdUsingMath(sample))
#     timemat.append(time.time()-start)

# print("-----------------")
# print(f"time list: {sum(timelist)/len(timelist)}")
# print(f"time math: {sum(timemat)/len(timemat)}")
