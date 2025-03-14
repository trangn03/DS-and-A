class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def divides(s, t):
            """
            Checks if string 't' divides string 's' (i.e., s is formed by repeating t).

            Args:
                s: The string to check divisibility of.
                t: The potential divisor string.

            Returns:
                True if t divides s, False otherwise.
            """
            if len(s) % len(t) != 0:  # If s's length is not a multiple of t's length, t cannot divide s
                return False
            return s == t * (len(s) // len(t))  # Check if s is formed by repeating t the correct number of times

        # Iterate through possible divisor lengths, starting from the longest
        for length in range(min(len(str1), len(str2)), 0, -1):
            # Optimization: Check if both string lengths are divisible by the current length
            if len(str1) % length == 0 and len(str2) % length == 0:
                potential_divisor = str1[:length]  # Extract the potential divisor from the beginning of str1
                # Check if the potential divisor divides both str1 and str2
                if divides(str1, potential_divisor) and divides(str2, potential_divisor):
                    return potential_divisor  # Return the divisor if it divides both strings

        return ""  # Return an empty string if no common divisor is found