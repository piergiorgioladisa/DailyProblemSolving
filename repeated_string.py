#!/bin/python3

# Complete the repeatedString function below.
def repeatedString(s, n):
    counter_in_string = 0
    total_counter = 0
    for char in s:
        if char == 'a':
            counter_in_string += 1
    
    total_counter = counter_in_string * (n // len(s))
    remainder = n % len(s) 

    for i in range(remainder):
        if s[i] == 'a':
            total_counter += 1
    


    return total_counter


if __name__ == '__main__':
  
    s = 'aba'
    n = 100
    result = repeatedString(s, n)
    print(result)
