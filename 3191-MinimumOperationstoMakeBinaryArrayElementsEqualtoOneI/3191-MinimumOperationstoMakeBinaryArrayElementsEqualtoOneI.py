# Last updated: 3/26/2025, 9:30:01 PM
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                count += 1
                if i + 1 >= n or i + 2 >= n:
                    return -1
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
        return count 
        