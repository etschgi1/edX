def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.

        BAG 3 IS WHATS OUT!!!
    """

    items = [1, 2, 3]
    N = len(items)
    for i in range(3**N):
        bucket1 = []
        bucket2 = []
        bucket3 = []
        for j in range(N):
            # test bit jth of integer i
            if (i//3**j) % 3 == 0:
                bucket1.append(items[j])
            elif (i//3**j) % 3 == 1:
                bucket2.append(items[j])
            elif (i//3**j) % 3 == 2:
                bucket3.append(items[j])
        yield(bucket1, bucket2, bucket3)
