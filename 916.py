class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def isSubset(word: str, subset: str) -> bool:
            word_list = list(word)
            for letter in subset:
                if letter in word_list:
                    word_list.remove(letter)
                else:
                    return False
            return True

        def generateSubset(words2: List[str]) -> str:
            combined_subset = words2[0]
            for word in words2[1:]:
                for letter in word:
                    if word.count(letter) > combined_subset.count(letter):
                        combined_subset += letter
            return combined_subset

        subset = generateSubset(words2)
        return [word for word in words1 if isSubset(word, subset)]
