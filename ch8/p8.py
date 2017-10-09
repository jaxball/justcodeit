"""
Permutation with Dups: Write a method to compute all permutations of a string whose characters are not necessarily unique. The list of permutations should not have duplicates.
"""
from collections import Counter

def findPermsDup(instr):
	permsDup = []
	freqmap = dict(Counter(instr))
	genPerms(freqmap, "", len(instr), permsDup)
	return permsDup

def genPerms(fmap, prefix, remLength, permutations):
	if remLength == 0:
		permutations.append(prefix)
		return

	for c in fmap:
		if fmap[c] > 0:
			fmap[c] -= 1
			genPerms(fmap, prefix+c, remLength-1, permutations)
			fmap[c] += 1




# Test cases: 
print findPermsDup("aaf")
# print [perm.strip() for perm in allPerms]

# CTCI Solution: 
"""
def printPerms(string):
    result = []
    letterCountMap = buildFreqTable(string)
    printPermsInner(letterCountMap, "", len(string), result)
    return result

#returns dictionary <string, integer>
def buildFreqTable(string):
    letterCountMap = {}
    for letter in string:
        if letter not in letterCountMap:
            letterCountMap[letter] = 0
        letterCountMap[letter] += 1
    print "map =", letterCountMap
    return letterCountMap

def printPermsInner(letterCountMap, prefix, remaining, result):
    #base case Permutation has been completed
    if remaining == 0:
        result.append(prefix)
        return
    #try remaining letter for next char, and generate remaining permutations
    for character in letterCountMap:
        count = letterCountMap[character]
        if count > 0:
            letterCountMap[character] -= 1
            printPermsInner(letterCountMap, prefix + character, remaining - 1, result)
            letterCountMap[character] = count

print(printPerms("aaf"))
"""