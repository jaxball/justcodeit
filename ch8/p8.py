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