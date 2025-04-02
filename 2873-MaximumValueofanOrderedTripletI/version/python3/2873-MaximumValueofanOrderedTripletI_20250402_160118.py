# Last updated: 4/2/2025, 4:01:18 PM
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # Three pointers
        n = len(nums)
        left = [0] * n
        right = [0] * n
        for i in range (n - 1):
            left[i + 1] = max(left[i], nums[i])
            right[n - 2 - i] = max(right[n - i - 1], nums[n - i - 1])
        return max(0, max((left[i] - nums[i]) * right[i] for i in range(1, n-1)))
        