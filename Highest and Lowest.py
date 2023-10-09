"""
Highest and Lowest

DESCRIPTION:
In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first.
"""


# My solution

def high_and_low(numbers):
    res = [int(i) for i in numbers.split(' ')]
    return f'{max(res)} {min(res)}'


# OR:

def high_and_low(numbers):
    numbers = numbers.split(' ')
    lst = []
    for i in numbers:
        i = int(i)
        lst.append(i)
    return f'{max(lst)} {min(lst)}'


"""
Best Practices

#1
def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
    
#2
def high_and_low(numbers):
  numbers = [int(c) for c in numbers.split(' ')]
  return f"{max(numbers)} {min(numbers)}"
  
"""
