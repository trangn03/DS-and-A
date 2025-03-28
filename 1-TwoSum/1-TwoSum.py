# Last updated: 3/28/2025, 3:23:40 PM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Check if the length of two strings are equal. 
        # If they are not then they cannot be isomorphic -> return False 
        if len(s) != len(t):
            return False 
        # Mapping rules
        # Initialize two maps to store characters as keys and their indexes as values
        # Dictionary stores the mapping from characters in s to their corresponding characters in t. 
        # in s = "egg" and t = "add", s_to_t would eventually contain {'e': 'a', 'g': 'd'}.
        s_t = {}
        
        # Stores the reverse mapping, from characters in t to their corresponding characters in s.
        t_s = {}
        
        # For each character pair char_s and char_t at same index i
        for i in range(len(s)):
            # Get the characters at the current index i from both strings.
            char_s = s[i]
            char_t = t[i]
            
            # Check s_t 
            # If char_s is already in s_t, check if its mapped the character is same as current character
            # else add the mapping
            if char_s in s_t:
                if s_t[char_s] != char_t:
                    return False
            else:
                s_t[char_s] = char_t
            # Check t_s 
            # If char_t is already in t_s, check if its mapped the character is same as current character
            # else add the mapping
            if char_t in t_s:
                if t_s[char_t] != char_s:
                    return False 
            else:
                t_s[char_t] = char_s
        return True