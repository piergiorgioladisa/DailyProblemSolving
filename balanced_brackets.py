#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    opening = ["{","[","("]
    closing = ["}","]",")"]
    if len(s) == 0:
        return "YES"
    if len(s) > 1000:
        return "NO"
    else:
        for char in s:
            #print("Char to examine", char)
            if char in opening:
                stack.append(char)
            if char in closing and len(stack) > 0:
                if char == closing[0] and stack[-1] == opening[0]:
                    stack.pop()
                elif char == closing[1] and stack[-1] == opening[1]:
                    stack.pop()
                elif char == closing[2] and stack[-1] == opening[2]:
                    stack.pop()
                else:
                    return "NO"
    if len(stack) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = ["{[()]}", "{[(])}", "{{[[(())]]}}"]

    for t_itr in range(len(t)):
        s = t[t_itr]
        result = isBalanced(s)
        print(result)
        
