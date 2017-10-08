"""
Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
"""
import sys

def tripleStep(n):

    memo = [0 for c in range(n+1)]
    memo[0] = 1
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4

    # suggestion: if checks and sets memo[n] only once for n = 1, 2, 3
    # i.e. don't hardcode return values
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4

    for i in range(4, n+1):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]

    return memo[n]

# Test cases
print tripleStep(int(sys.argv[1]))

