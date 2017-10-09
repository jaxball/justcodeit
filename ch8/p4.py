"""
Power Step: Write a method to return all subsets of a set.
"""

# Question in solution: There are 2^n subsets and each of the n elements will be contained in 
# half of the subsets (which 2^n-1 subsets). 

def powerStep(in_set, start): 
    """ generate/build all subsets of a given set. """
    # note: subsets disregard order of elements
    res = []
    if len(in_set) == start:
        #base case - add empty set
        if [] not in res:
            res.append([])
    else:
        res = powerStep(in_set, start+1)
        item = in_set[start]
        moreSubsets = []
        for subset in res:
            newSubset = []
            [newSubset.append(value) for value in subset if value not in newSubset]
            newSubset.append(item)
            print "newSubset =", newSubset
            moreSubsets.append(newSubset)
        print "moresubsets before recurse ends =", moreSubsets
        [res.append(subset) for subset in moreSubsets]
    return res


# Test cases:
print powerStep([1,2,3,4],0)