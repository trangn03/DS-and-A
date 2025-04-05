# Last updated: 4/4/2025, 8:42:50 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        # Go through list of num1 
        # If there is num1 in num2
        # Add that num to result 
        for num in nums1:
            if num in nums2 and num not in result:
                result.append(num)
        return result 
        