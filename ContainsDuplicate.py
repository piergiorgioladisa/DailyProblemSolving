"""
Given an array of integers, find if the array contains any duplicates.
"""

def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for item in nums:
            hashset.add(item)
            
        if len(hashset) == len(nums):
            return False
        else:
            return True
