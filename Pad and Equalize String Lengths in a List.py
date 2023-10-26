"""
Pad and Equalize String Lengths in a List

At the input we have a list of strings of different lengths.
You need to write a function all_eq(lst) that will return a new list of strings of the same length.
The length of the final line is determined based on the largest of them.
If a particular line is shorter than the longest one,
pad it with underscores from the right edge to the required number of characters.

The arrangement of the elements of the initial list does not change.
"""

# My solution

def all_eq(lst):
    max_len = 0
    new_lst = []
    for i in lst:
        if max_len < len(i):
            max_len = len(i)
        else:
            i = i+('_'*(max_len - len(i)))
        new_lst.append(i)
    return new_lst

"""
Best Practices

def all_eq(lst):
    max_item = max(lst, key=lambda x: len(x))
    max_len = len(max_item)
    return [item.ljust(max_len, '_') for item in lst]

"""
