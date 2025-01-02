class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel(letter: str) -> bool:
            return letter in 'aeiou'
        
        def is_valid(word: str) -> bool:
            return is_vowel(word[0]) and is_vowel(word[-1])
        
        n = len(words)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if is_valid(words[i]) else 0)
        
        ans = []
        for li, ri in queries:
            ans.append(prefix[ri + 1] - prefix[li])
        
        return ans
