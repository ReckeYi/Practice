"""
Stop gninnipS My sdroW!

DESCRIPTION:
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"
"""


# My solution
def spin_words(sentence):
    sentence = sentence.split()
    new_sentence = []
    for i in sentence:
        if len(i) >= 5:
            new_sentence.append(i[::-1])
        else:
            new_sentence.append(i)
    return ' '.join(new_sentence)


# OR

def spin_words(sentence):
    new_sentence = [word[::-1] if len(word) >= 5 else word for word in sentence.split()]
    return ' '.join(new_sentence)


"""
Best Practices

#1
def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
    
#2
def spin_words(sentence):
    words = [word for word in sentence.split(" ")]
    words = [word if len(word) < 5 else word[::-1] for word in words]
    return " ".join(words)
"""
