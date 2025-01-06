class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        length = len(boxes)
        answer = []

        for i in range(length):
            count = 0
            for j in range(length):
                if boxes[j] == '1':
                    count += abs(i - j)
            answer.append(count)
    
        return answer
