class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointer
        # Convert to lowercase
        left = 0
        right = len(s) - 1 
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -=1
            # Check for if two string are the same alphanumeric
            if left < right: 
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True
