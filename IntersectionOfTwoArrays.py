"""
Given two arrays, write a function to compute their intersection.
"""

def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashset = set()
        output = []
        
        for item in nums1:
            hashset.add(item)
            
        for item in nums2:
            if item in hashset and not item in output:
                output.append(item)
                
        return output
