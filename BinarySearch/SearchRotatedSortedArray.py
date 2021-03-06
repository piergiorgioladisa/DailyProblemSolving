"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).
"""

def search(nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums)-1
        i = -1  # count iterations
        
        while left <= right:
            mid = (left + right)//2 
            print("[",left,",",right,"]", "MID",mid)
            
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
    
