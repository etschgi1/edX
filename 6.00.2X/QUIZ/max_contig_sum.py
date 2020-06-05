def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    # from every number get subsets:
    out = []
    # start at every number
    for start in range(len(L)):
        # get slice for from start number to end which is first start num and goes up to len(L)
        for end in range(start+1, len(L)+1):
            out.append(L[start:end])
    # get max from individual sums in out
    return max([sum(ss) for ss in out])


print(max_contig_sum([3, 4, -8, 15, -1, 2]))
