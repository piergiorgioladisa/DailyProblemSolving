"""

"""

def twoStrings(s1, s2):
    string1 = set(s1)
    string2 = set(s2)

    intersection = string1 & string2
    if len(intersection) > 0:
        return "YES"
    else:
        return "NO"
    

if __name__ == '__main__':
   
    q = 4
    strings_list = ["wouldyoulikefries","abcabcabcabcabcabc", "hackerrankcommunity", 
                    "cdecdecdecde","jackandjill","wentupthehill","writetoyourparents","fghmqzldbc"]
    idx = 0
    for q_itr in range(q):
        s1 = strings_list[idx]
        s2 = strings_list[idx]
        idx += 2
        result = twoStrings(s1, s2)
        print(result + '\n')
