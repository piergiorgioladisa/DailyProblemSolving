"""
The function must return an integer representing the
minimum total characters that must be deleted to make 
the strings anagrams.

makeAnagram has the following parameter(s):

    a: a string
    b: a string

"""

def makeAnagram(a, b):
    setA = set(a)
    setB = set(b)
    intersection = setA & setB  # letters in common
    to_remove = 0
    for i in a:
        if i not in intersection:
            to_remove +=1
    for i in b:
        if i not in intersection:
            to_remove +=1
    for i in intersection:
        a_excess = list(a).count(i)
        b_excess = list(b).count(i)
        if a_excess > b_excess:
            to_remove += a_excess - b_excess
        elif a_excess < b_excess:
            to_remove += b_excess - a_excess
    return to_remove

if __name__ == '__main__':
    
    a = "fcrxzwscanmligyxyvym"
    b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"
    res = makeAnagram(a, b)
    print(str(res) + '\n')
