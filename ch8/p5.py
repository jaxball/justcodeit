"""
Recursive Multiply: Write a recursive function to multiply two positive integers without using the * operator 
(or / operator). You can use addition, subtraction, and bit shifting, but you should minimize the number of 
those operations. 
"""

def recursiveProd(num1, num2):
    bigger = num1 if num1 >= num2 else num2 #var = something if condition else something_else
    smaller = num2 if num2 < num1 else num1

    return recursiveMult(smaller, bigger)

def recursiveMult(s, b):
    # base case for terminating recursion
    if s == 0: 
        return 0
    elif s == 1:
        return b

    halfs = s >> 1
    halfProd = recursiveMult(halfs, b)
    if s % 2 == 0:
        return halfProd + halfProd
    elif s % 2 == 1: 
        return halfProd + halfProd + b 

# Test Cases:
print recursiveProd(5,3)