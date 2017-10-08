"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can
only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on
them. Design an algorithm to find a path for the robot from the top left to the bottom right.
"""

# m = rows
# n = columns
def robotGrid(m, n):

    memo = [[0 for c in range(n)] for r in range(m)]
    memo[0][0] = 1
    for i in range(1, m):
        memo[i][0] = memo[i-1][0]+1
    for j in range(1, n):
        memo[0][j] = memo[0][j-1]+1


    for i in range(1, n-1):
        for j in range(1, m-1):
            memo[j][i] = min(memo[j-1][i], memo[j][i-1]) + 1

    print memo

# Test cases
robotGrid(4, 5)