class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = len(s) * [0];
        modified_list = []

        for shift in shifts:
            for i in range(shift[0], shift[1] + 1):
                if shift[2]:
                    prefix[i] += 1
                else:
                    prefix[i] -= 1
            
        for i in range(len(s)):
            new_char = chr((ord(s[i]) - 97 + prefix[i]) % 26 + 97)
            modified_list.append(new_char)
    
        return ''.join(modified_list)
