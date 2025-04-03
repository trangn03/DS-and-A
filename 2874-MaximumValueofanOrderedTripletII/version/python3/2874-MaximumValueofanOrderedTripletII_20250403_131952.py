# Last updated: 4/3/2025, 1:19:52 PM
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        highest = 0
        diff = 0
        result = 0

        for num in nums:
            if diff * num > result:
                result = diff * num
            if highest - num > diff:
                diff = highest - num
            if num > highest:
                highest = num
        return result
        