# Last updated: 4/6/2025, 12:05:11 AM
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res |= i
        return res * (1 << (len(nums) - 1))
        