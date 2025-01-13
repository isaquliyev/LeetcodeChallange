class Solution:
    def minimumLength(self, s: str) -> int:
        disclosed_characters = []
        count = 0


        for i in s:
            if i in disclosed_characters:
                pass
            else:
                temp = s.count(i)
                while temp >= 3:
                    temp -= 2
                disclosed_characters.append(i)
                count += temp
        
        return count
