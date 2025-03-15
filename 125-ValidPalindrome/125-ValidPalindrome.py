class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanum_string = ""
        for c in s:
            if c.isalnum():
                alphanum_string = alphanum_string + c.lower()
                                
        return alphanum_string == alphanum_string[::-1]