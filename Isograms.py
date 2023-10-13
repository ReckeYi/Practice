"""

Isograms

DESCRIPTION:
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false

"""


# My solution
def is_isogram(string):
    return len(string) == len(set(string.lower()))


# OR

def is_isogram(string):
    new_string = ''
    for i in string.lower():
        if i.lower() not in new_string:
            new_string = new_string + i

    if len(string) == len(new_string):
        return True
    else:
        return False


"""
Best Practices

#1
def is_isogram(string):
    return len(string) == len(set(string.lower()))
    
#2
def is_isogram(string):
    string = string.lower()
    for letter in string:
        if string.count(letter) > 1: return False
    return True
"""
