
""" Subarray Sum (nonnegative): Given an unsorted array of nonnegative integers, find a continous subarray which adds to a given number. """

def subSum(arr, sum):

    curr_sum = arr[0] 
    start_idx = 0

    for i in range(1, len(arr)):

        while curr_sum>sum and start_idx < i-1:
            # remove trailing elements while curr_sum > sum
            curr_sum -= arr[start_idx]
            start_idx += 1

        if curr_sum == sum:
            print "sum found between index", start_idx, "and", i
            return

        curr_sum += arr[i]

    return

subSum([1,4,20,3,10,5], 33)