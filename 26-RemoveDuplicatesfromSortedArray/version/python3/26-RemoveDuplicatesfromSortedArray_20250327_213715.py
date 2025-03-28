# Last updated: 3/27/2025, 9:37:15 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # Pointer for unique element
        index = 1
        # # Iterate through the array starting from the second element
        for j in range(1, len(nums)):
            # # If the current element is different from the previous one
            if nums[j] != nums[j-1]:
                # Overwrite the element at index i with the unique element
                nums[index] = nums[j]
                # Move the unique element pointer forward
                index += 1
        return index
