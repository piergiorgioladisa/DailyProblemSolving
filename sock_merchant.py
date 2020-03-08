#!/bin/python3

'''
  DESCRIPTION:
  
  John works at a clothing store. He has a large pile of socks that he must pair 
  by color for sale. Given an array of integers representing the color of each 
  sock, determine how many pairs of socks with matching colors there are.
  For example, there are n=7 socks with colors ar=[1,2,1,2,3,1,2]. There is one 
  pair of color 1 and one of color 2. There are three odd socks left, one of each 
  color. The number of pairs is 2. 
'''

# Complete the sockMerchant function below.
def sockMerchant(n, ar):

    uniques = []
    pairs = 0
    for i in range(n):              # store the unique elements 
        if ar[i] in uniques:        # in an array
            continue
        else:
            uniques.append(ar[i])
    
    for elem in uniques:              # check the pair for each uniques
        counter = 0
        for i in ar:
            if elem == i:
                counter += 1
        pairs += (counter // 2)
    return pairs




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    
    result = sockMerchant(n, ar)

    print(result)
