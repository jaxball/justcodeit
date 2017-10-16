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

def searchLeftRight(left, right, beg, curr, line, res):
    while left > 0: 
        if line[left] == beg or line[left] == curr:
            res.insert(0, line[left])
        else:
            break
        left -= 1

    while right < len(line)-1: 
        if line[right] == beg or line[right] == curr:
            res.append(line[right])
        else:
            break
        right += 1

def LCSdistinct(line):
    
    if len(line) < 2: 
        return ""

    maxString = []
    res = []
    beg = ""
    curr = ""
    maxLen = 0
    # beg = line[0]
    # i = 1
    # res.append(beg)

    # left = 0
    # right = 0 

    # currLen = 0
    # while line[i] == beg and i < len(line)-1:
    #     currLen += 1
    #     i += 1
    # curr = line[i]
    # res.append(curr)


    for i, c in enumerate(line[2:]):
        # print "beginnig of loop", c, beg, curr
        if c == beg or c == curr:
            res.append(c)
            continue
        else: 
            right = i + 2
            left = right - len(res) - 1
            
            searchLeftRight(left, right, beg, curr, line, res)
            # while left > 0: 
            #     if line[left] == beg or line[left] == curr:
            #         res.insert(0, line[left])
            #         currLen += 1
            #     else:
            #         break
            #     left -= 1

            # while right < len(line)-1: 
            #     if line[right] == beg or line[right] == curr:
            #         res.append(line[right])
            #         currLen += 1
            #     else:
            #         break
            #     right += 1

            maxLen = max(maxLen, len(res))
            if maxLen == len(res):
                maxString = res

            res = []            
            beg = line[i+2-1]
            curr = c
            # res.append(beg)
            # res.append(curr)

    right = i + 2
    left = right - len(res) 
    searchLeftRight(left, right, beg, curr, line, res)

    currLen = len(res)
    maxLen = max(maxLen, currLen)
    if maxLen == currLen:
        maxString = res

    return ''.join(maxString)

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
