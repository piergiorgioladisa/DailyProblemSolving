"""
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.
You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

"""

def guessNumber(n: int) -> int:
        
        left, right = 0, n
        
        while True:
            mid = (left + right) // 2
            response = guess(mid)
            if response == - 1:
                right = mid - 1
            elif response == 0:
                return mid
            else:
                left = mid + 1
                
