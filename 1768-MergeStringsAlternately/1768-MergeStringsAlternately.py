class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        w1 = len(word1)
        w2 = len(word2)
        result = []
        while left < w1 or right < w2:
            if left < w1:
                result += word1[left]
                left += 1
            if right < w2:
                result += word2[right]
                right += 1
        return "".join(result)
        