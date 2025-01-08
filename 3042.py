class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        length = len(words)


        for i in range(length):
            for j in range(i + 1, length):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1
            
        return count
