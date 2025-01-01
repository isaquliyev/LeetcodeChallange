class Solution:
    def maxScore(self, s: str) -> int:
        length = len(s)
        maxi = 0

        for i in range(1, length):
            if maxi < s[i:length].count('1') + s[:i].count('0'):
                maxi = s[i:length].count('1') + s[:i].count('0')
            else:
                pass
        return maxi
