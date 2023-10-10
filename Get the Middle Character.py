"""
Get the Middle Character

You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
#Input

A word (string) of length 0 < str < 1000 (In javascript you may get slightly more than 1000 in some test cases due to an error in the test cases). You do not need to test for this. This is only here to tell you that you do not need to worry about your solution timing out.

#Output

The middle character(s) of the word represented as a string.
"""


# My solution
def get_middle(word):
    mid = len(word) // 2
    return ''.join([word[mid]] if len(word) % 2 != 0 else [word[mid - 1], word[mid]])


# OR

def get_middle(word):
    mid = len(word) / 2
    first = mid - 0.5
    second = mid + 0.5
    if len(word) % 2 != 0:
        return f'{word[int(first)]}'
    else:
        return f'{word[int(first)]}{word[int(second)]}'


"""
Best Practices

#1
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]
    
#2
def get_middle(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s
"""
