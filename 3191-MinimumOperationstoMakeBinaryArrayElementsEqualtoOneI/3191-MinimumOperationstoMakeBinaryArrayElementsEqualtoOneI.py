class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # Array, Hash table
        # Initialize a counter collection
        counter = collections.Counter(nums)
        # Loop through the array
        # Mod (even - odd)
        for value in counter.values():
            if value % 2 == 1:
                return False 
        return True        