import sys

def subarraySumClosest(nums):
        # write your code here
        if not nums:
            return None
        if len(nums) == 1:
            return [0,0]
        sums = [0 for i in range(len(nums))]
        sums[0] = nums[0]
        for i in range(1, len(nums)):
            sums[i] = sums[i-1] + nums[i]

        sortedSums = list(sums)
        sortedSums.sort()

        minDiff = sys.maxint
        for i in range(1, len(sortedSums)):
            if sortedSums[i] - sortedSums[i-1] < minDiff:
                minDiff = sortedSums[i] - sortedSums[i-1]
                num1 = sortedSums[i-1]
                num2 = sortedSums[i]
        index1 = sums.index(num1)
        index2 = sums.index(num2)
        if index1 > index2:
            tmp = index1
            index1 = index2 + 1
            index2 = tmp
        else:
            index1 = index1 + 1
        return [index1, index2]


def  closest_subtring(intList, n):

    left = 0 
    right = len(intList) - 1
   
    # intList = intList.sort()
        
    num = [2,4,6]
    hello = num[1] + num[2]
    print intList[1] + intList[2]
    print intList
    print hello
    # while left < right:
        # tsum = intList[left] + intList[right]
        # print tsum
        # if tsum == n:
        #     return (left, right)
        # elif 2*intList[left] == n:
        #     return (left, left)
        # elif 2*intList[right] == n:
        #     return (right, right)
        # elif tsum > n: 
        #     right -= 1
        # elif tsum < n:
        #     left += 1
            
    return None

def length_max_subarray(array, K):
    head, tail = 0, 0
    length = 0
    current_sum = 0
    while(tail<len(array)):
        if current_sum + array[tail]<=K:
            current_sum += array[tail]
            tail+=1
            if tail-head > length:
                length = tail-head
        else:
            current_sum -= array[head]
            head+=1

    return length

s1 = [3,4,5,6,7]
s2 = [-3, 1, 1, -3, 5]
s3 = [1, 2, 5, -3, 10, 5]
# print closest_subtring([3,4,5,6,7], 14) 
# print length_max_subarray(s1, 14)
print subarraySumClosest(s3)