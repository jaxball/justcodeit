"""
Parens: Implement an algorithm to print all valid (i.e., properly opened and closed) combinations of n pairs of parentheses. 
EXAMPLE
Input: 3
Output: ((())), (()()), (())(), ()(()), ()()()
"""

def permParens(n):
	perms = []
	genParens(perms, n, n, [0]*2*n, 0)
	return perms

def genParens(perms, leftrem, rightrem, parenBuilder, idx):

	if leftrem < 0 or rightrem < leftrem: 
		return

	if leftrem == 0 and rightrem == 0:
		parenStr = "".join(parenBuilder)
		perms.append(parenStr)
	else:
		# parenBuilder.append("(")
		parenBuilder[idx] = "("
		genParens(perms, leftrem-1, rightrem, parenBuilder, idx+1)

		# parenBuilder.append("(")
		parenBuilder[idx] = ")"
		# parenBuilder[-1] = ")"
		genParens(perms, leftrem, rightrem-1, parenBuilder, idx+1)


# Test cases
print "n=1,", permParens(1)
print "n=2,", permParens(2)
print "n=3,", permParens(3)
# print "n=21,", permParens(6)	# check: (()(()))()() is valid