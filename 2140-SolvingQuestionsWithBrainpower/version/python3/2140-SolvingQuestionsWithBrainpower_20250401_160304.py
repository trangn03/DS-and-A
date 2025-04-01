# Last updated: 4/1/2025, 4:03:04 PM
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        total = [0] * n
        prev = questions[-1][0]

        for i in range (n-1,-1,-1):
            total[i] = prev
            point, skip = questions[i]
            j = i + skip + 1
            if j < n:
                point += total[j]
            if point > prev:
                total[i] = point
            prev = total[i]
        return total[0]
        