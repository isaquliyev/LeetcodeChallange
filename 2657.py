class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        length = len(A)
        new_array = []

        for i in range(length):
            new_array.append(2 * (i + 1) - len(set(A[:i + 1] + B[:i + 1])))

        return new_array
