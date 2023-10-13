"""
Exes and Ohs

DESCRIPTION:
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""


# My solution

def xo(s):
    x_s = 0
    o_s = 0
    for i in s.lower():
        if i == "x":
            x_s += 1
        if i == "o":
            o_s += 1
    if x_s == o_s:
        return True
    else:
        return False


# OR

def xo(s):
    return s.lower().count("x") == s.lower().count("o")


"""
Best Practices

#1
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
    
#2
def xo(s):
    return s.lower().count('x') == s.lower().count('o')
"""
