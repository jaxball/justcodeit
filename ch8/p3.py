"""
Magic Index: A magic index in an array A[1...n-1] is defined to be an index such that A[i] = i. Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A. 
FOLLOW UP 
What if the values are not distinct?
"""

# Distinct array of integers 
def magicIndex(arr, start, end):
	if start > end: 
		return None

	mid = start+((end-start)/2)
	# print "mid=", mid
	if arr[mid] == mid:
		return mid
	elif arr[mid] > mid: 
		# search first half
		return magicIndex(arr, start, mid-1)
	else: 
		return magicIndex(arr, mid+1, end)


# Distinct array of integers 
def magicIndexAdvanced(arr, start, end):
	if start > end: 
		print start, end
		return 

	mid = start+((end-start)/2)
	if arr[mid] == mid:
		return mid

	left = min(mid-1, arr[mid])
	right = max(mid+1, arr[mid])
	# print "left, right, start, end, mid= ", left, right, start, end, mid
	return magicIndex(arr, start, left) or magicIndex(arr, right, end)
	
# Test cases:
		#  0 1 2 3 4 5  6 
inArray = [0,1,3,5,6,7,10]	# ans = 1
		#  0 1 2 3 4 5 6 
inArrDup =   [0,2,3,5,5,5,8] # ans = 5

ans = magicIndex(inArray, 0, len(inArray))
ans2= magicIndexAdvanced(inArrDup, 0, len(inArray))
print "distinct array =", ans
print "non-distinct array =", ans2