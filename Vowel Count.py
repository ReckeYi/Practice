"""
Vowel Count

DESCRIPTION:
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


# My solution

def get_count(sentence):
    vowels = 'a e i o u'.split(' ')
    count = 0
    for i in sentence:
        if i in vowels:
            count += 1
    return count


"""
Best Practices

#1
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")
    
#2
def getCount(s):
    return sum(c in 'aeiou' for c in s)
"""
