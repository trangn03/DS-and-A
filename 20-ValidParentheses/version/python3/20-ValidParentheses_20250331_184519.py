# Last updated: 3/31/2025, 6:45:19 PM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesis = {")" : "(", "]" : "[", "}" : "{"}

        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack or stack.pop() != parenthesis[char]:
                    return False
        return len(stack) == 0

        