# Last updated: 3/28/2025, 2:54:14 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sell = set()
        for i in nums:
            if i in sell:
                return True
            sell.add(i)
        return False

            

               
        