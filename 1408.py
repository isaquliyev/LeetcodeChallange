class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        merged_words = '/'.join(words)
        answer = []


        for word in words:
            if merged_words.count(word) > 1:
                answer.append(word)
        
        return answer
