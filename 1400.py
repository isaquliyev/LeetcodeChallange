class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        letters = set(list(s))

        prefix = []

        for letter in letters:
            prefix.append(s.count(letter))
        
        number_of_odds = 0
        for number in prefix:
            if number % 2 == 1:
                number_of_odds += 1
        
        return number_of_odds <= k and k <= len(s)
