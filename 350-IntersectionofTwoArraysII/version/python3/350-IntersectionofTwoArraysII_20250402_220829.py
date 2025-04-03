# Last updated: 4/2/2025, 10:08:29 PM
# Dictionary (hashmap) problem
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1 = {}  # Initialize a dictionary to store element counts from nums1
        for num in nums1:
            counts1[num] = counts1.get(num, 0) + 1  # Count occurrences of each element in nums1

        result = []  # Initialize an empty list to store the intersection
        for num in nums2:
            if num in counts1 and counts1[num] > 0:  # Check if num exists in counts1 and has a count > 0
                result.append(num)  # Add num to the result if it's in the intersection
                counts1[num] -= 1  # Decrement the count of num in counts1

        result.sort()  # Sort the result list in ascending order
        return result

        