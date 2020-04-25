sample = ["tes", "miauh", "foooooo"]


def stdDevOfLengths(s):
    """
    s: a List of sample inputs
    returns a float, the sandard deviation of the lengths of strings in list,
    NaN if L is empty.
    """
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


print(stdDevOfLengths(sample))
