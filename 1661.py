class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        row_paint = [0] * m
        col_paint = [0] * n

        num_to_pos = {mat[i][j]: (i, j) for i in range(m) for j in range(n)}

        for i, num in enumerate(arr):
            r, c = num_to_pos[num]
            row_paint[r] += 1
            col_paint[c] += 1

            if row_paint[r] == n or col_paint[c] == m:
                return i
