class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Empty string
        if not strs:
            return ""
        prefix = strs[0]
        for i in strs[1:]:
            while not i.startswith(prefix) and prefix:
                prefix = prefix[:-1]
            if not prefix:
                return ""
        return prefix




        