"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be 
traced back to him through his handwriting. He found a magazine and wants to know 
if he can cut out whole words from it and use them to create an untraceable replica 
of his ransom note. The words in his note are case-sensitive and he must use only 
whole words available in the magazine. He cannot use substrings or concatenation to 
create the words he needs.
Given the words in the magazine and the words in the ransom note, print Yes if he can 
replicate his ransom note exactly using whole words from the magazine; otherwise, print No.

For example, the note is "Attack at dawn". The magazine contains only "attack at dawn". 
The magazine has all the right words, but there's a case mismatch. The answer is No. 

"""

def checkMagazine(magazine, note):
    if len(note)>len(magazine):
        print("No")
        return
    mgz_dict = {}
    note_dict = {}
    for word in magazine:
        mgz_dict[word] = magazine.count(word)
    for word in note:
        if word in mgz_dict.keys():
            if note.count(word) <= mgz_dict[word]:
                note_dict[word] = True
            else:
                note_dict[word] = False
        else:
            print("No")
            return
    if all(x==True for x in note_dict.values()):
        print("Yes")
        return
    else:
        print("No")
        return
        
        
if __name__ == '__main__':
    mn = input().split()

    m = 6

    n = 4

    magazine = ['give', 'me', 'one', 'grand', 'today', 'night']

    note = ['give', 'one', 'grand']

    checkMagazine(magazine, note)
