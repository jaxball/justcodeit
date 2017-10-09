"""
Permutation without Dups: Write a method to compute all permutations of a string of unique characters.
"""

# Failed attempt 
"""
def permUnique(instr):
	permutations = []
	permutations.append("")
	permuteHelper(instr, 0, permutations)
	return permutations


def permuteHelper(instr, idx, res):

	if idx > len(instr)-1: 
		return

	print "before =", res
	for item in res:
		newPerm = item + instr[idx]
		print "newPerm =", newPerm, "item =", item 
		res.append(newPerm)
		print "res is", res		
		# for i in range(idx, len(instr)-idx-1):
		return permuteHelper(instr, idx+1, res)

	return
"""

def findPerms(instr):
	print "in FindPerms", instr
	if instr == None:
		return None

	permutations = [] 
	if len(instr) == 0: 
		# make sure it has a space in between! otherwise in 
		# tail recursive call no characters will be added
		permutations.append(" ") 
		return permutations

	firstLetter = instr[0]
	subPerms = findPerms(instr[1:])
	for substr in subPerms:
		for i in range(0, len(substr)):
			newPerm = substr[:i] + firstLetter + substr[i:]
			permutations.append(newPerm)			

	return permutations

# Test cases: 
print findPerms("hello")
print findPerms("str")
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