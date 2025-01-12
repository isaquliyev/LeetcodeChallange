class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        count = 0
        reverse_count = 0
        n = len(s)

        changeable = locked.count('0')

        for i in range(n):
            if s[i] == '(':
                count += 1
            else:
                count -= 1
            if s[n - i - 1] == '(':
                reverse_count += 1
            else:
                reverse_count -= 1
            if s[i] == ')' and locked[i] == '0':
                count += 2
            if s[n - i - 1] == '(' and locked[n - i - 1] == '0':
                reverse_count -= 2 
            if count < 0 or reverse_count > 0:
                return False
        
        if n % 2 == 1 or count > changeable * 2:
            return False
        else:
            return True
