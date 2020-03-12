"""
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
"""

def mySqrt(self, x: int) -> int:
        
        if x == 0:
            return 0
        if x == 1:
            return 1

        left, right = 0, x-1
        while left <= right:
            mid = (left + right) // 2
            if mid**2 == x :
                return mid
            elif mid**2 < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return left - 1
