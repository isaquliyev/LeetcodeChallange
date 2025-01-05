class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n + 1)

        for start, end, direction in shifts:
            prefix[start] += 1 if direction == 1 else -1
            prefix[end + 1] -= 1 if direction == 1 else -1
            
        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        result = []
        for i in range(n):
            new_char = chr((ord(s[i]) - ord('a') + prefix[i]) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)
