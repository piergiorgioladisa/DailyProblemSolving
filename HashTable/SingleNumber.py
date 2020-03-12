"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.
"""

def singleNumber(self, nums: List[int]) -> int:
        
        hashset = set()
        for item in nums:
            if item in hashset:
                hashset.discard(item)
            else:
                hashset.add(item)
        return hashset.pop()
        
