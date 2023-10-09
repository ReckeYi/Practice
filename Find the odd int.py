"""
Find the odd int

DESCRIPTION:
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""


# My solution
def find_it(seq):
    dct = {}
    n = 1
    for i in seq:
        if i in dct:
            dct[i] += n
        else:
            dct[i] = n
    for i in dct:
        if dct[i] % 2 != 0:
            return i


"""
Best Practices

#1
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
            
#2
def find_it(seq):
    return [x for x in seq if seq.count(x) % 2][0]
"""
