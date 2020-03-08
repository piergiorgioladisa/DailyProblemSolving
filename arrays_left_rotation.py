#!/bin/python3

# Complete the rotLeft function below.
def rotLeft(a, d):
    output = [0] * len(a)

    for i in range(len(a)):
        new_index = i - d
        if (new_index < 0):
            new_index = len(a) + new_index
        print(a[i], " goes to", new_index)
        output[new_index] = a[i]
    return output

if __name__ == '__main__':

    a = [1,2,3,4,5,6]
    d = 4
    
    print(a)
    result = rotLeft(a, d)
    print(result)

    
