"""
Search a target number inside a sorted array and return its index.
If it's not inside, return -1
"""

def search(nums: List[int], target: int) -> int:
        
        mid_index = len(nums) // 2
        
        if nums[mid_index] == target:
            return mid_index
        elif nums[mid_index] > target:
            for index in range(mid_index):
                if nums[index] == target:
                    return index
        elif nums[mid_index] < target:
            for index in range(mid_index+1, len(nums)):
                if nums[index] == target:
                    return index
        return -1
