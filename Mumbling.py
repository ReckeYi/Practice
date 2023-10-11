"""
Mumbling


DESCRIPTION:
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""


# My solution
def accum(word):
    lst = [char.upper() + char.lower() * index for index, char in enumerate(word)]
    return '-'.join(lst)


# OR

def accum(word):
    index = 0
    lst = []
    new_str = ''
    for i in word:
        index += 1
        multiple_letter = i * index
        lst.append(multiple_letter)
    for i in lst:
        new_str = (new_str + i + '-').title()
    return new_str[:-1:]


"""
Best Practices

#1
def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
    
#2
def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))
"""
