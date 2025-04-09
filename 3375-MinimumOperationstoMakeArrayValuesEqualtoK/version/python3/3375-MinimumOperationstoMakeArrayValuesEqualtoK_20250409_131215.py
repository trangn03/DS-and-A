# Last updated: 4/9/2025, 1:12:15 PM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Understand
        """
        int h valid if all values in the array that are > h
        select int h that is valid for curr values in nums
        for each index i where nums[i] > h
        return minimum number of operations to make every element in nums = to k
        """

        # Plan
        """
        hashmap problem
        """

        # Implement
        hashmap = defaultdict(int)
        for i in nums:
            if i < k: 
                return -1
            elif i > k:
                hashmap[i] += 1
        return len(hashmap)