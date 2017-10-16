""" Google practice problem (Stanford): 
Return the longest contiguous substring of 2 distinct characters from an input string.

Example
input: abbaacab
output: abbaa

input: abcefabbabaabefghghfa
return: abbabaab

input: aabceddddcdccecabceftg
return ddddcdcc

input: acbabbcbca
return: bbcbc

Additional edge case:
input: aabacbebebe
return: bebebe 

"""

def searchLeftRight(left, right, beg, end, line, window):
    while left >= 0: 
        if line[left] == beg or line[left] == end:
            window.insert(0, line[left])
        else:
            break
        left -= 1

    while right < len(line)-1: 
        if line[right] == beg or line[right] == end:
            window.append(line[right])
        else:
            break
        right += 1

def LCSdistinct(line):
    
    if len(line) < 2: 
        return ""

    maxString = []
    window = []
    beg = "" 
    end = ""

    for i, c in enumerate(line[:]):
        if c == beg or c == end:
            window.append(c)
            continue
        else: 
            right = i 
            left = right - len(window) - 1            
            searchLeftRight(left, right, beg, end, line, window)

            maxLen = max(len(maxString), len(window))
            if maxLen == len(window):
                maxString = window

            window = []            
            beg = line[i-1]
            end = c

    # Handles the case when string ends with the longest desired substring
    # right = i; left = right - len(window) 
    searchLeftRight(right, right+len(window), beg, end, line, window)

    maxLen = max(maxLen, len(window))
    if maxLen == len(window):
        maxString = window
    return ''.join(maxString)


# Test cases

s1 = "aabacbebebe"
s1b = "aabacbebebea"
s2 = "abbaacab"
s3 = "abcefabbabaabefghghfa"
s4 = "aabceddddcdccecabceftg"
s5 = "acbabbcbca"   # this case fails - FIXED by looking at both left and right for matches

print "s1 =", s1, "output =", LCSdistinct(s1)
print "s1b =", s1b, "output =", LCSdistinct(s1b)
print "s2 =", s2, "output =", LCSdistinct(s2)
print "s3 =", s3, "output =", LCSdistinct(s3)
print "s4 =", s4, "output =", LCSdistinct(s4)
print "s5 =", s4, "output =", LCSdistinct(s5)

assert LCSdistinct(s1) == "bebebe"
assert LCSdistinct(s2) == "abbaa", "Error on input = " + s2  + " (" + LCSdistinct(s2) + "). expected: abbaa"
assert LCSdistinct(s3) == "abbabaab"
assert LCSdistinct(s4) == "ddddcdcc"
assert LCSdistinct(s5) == "bbcbc"
