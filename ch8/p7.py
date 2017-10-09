"""
Permutation without Dups: Write a method to compute all permutations of a string of unique characters.
"""

def findPerms(instr):
	if instr == None:
		return None

	permutations = [] 
	if len(instr) == 0: 
		# make sure it has a space in between! otherwise in 
		# tail recursive call no characters will be added
		permutations.append(" ") 
		return permutations

	subPerms = findPerms(instr[1:])
	for substr in subPerms:
		for i in range(0, len(substr)):
			newPerm = substr[:i] + instr[0] + substr[i:]
			permutations.append(newPerm)			

	return permutations

# Test cases: 
allPerms = findPerms("hello")
print [perm.strip() for perm in allPerms]
allPerms = findPerms("str")
print [perm.strip() for perm in allPerms]

# CTCI Official Solution: 
"""
def getPerms2(string):
    result = []
    getPerms2Inner(" ", string, result)
    return result

def getPerms2Inner(prefix, remainder, result):
    if len(remainder) == 0:
        result.append(prefix)
    length = len(remainder)
    for i in range(length):
        before = remainder[:i]
        after = remainder[i+1:]
        c = remainder[i]
        getPerms2Inner(prefix + c, before + after, result)


print getPerms2("hello")
print getPerms2("str")
"""