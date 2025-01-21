class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefix_top = [0] * n
        prefix_bottom = [0] * n

        for i in range(n):
            prefix_top[i] = prefix_top[i - 1] + grid[0][i] if i > 0 else grid[0][i]
            prefix_bottom[i] = prefix_bottom[i - 1] + grid[1][i] if i > 0 else grid[1][i]

        min_second_robot = float('inf')

        for i in range(n):
            top_remaining = prefix_top[-1] - prefix_top[i]
            bottom_remaining = prefix_bottom[i - 1] if i > 0 else 0
            second_robot = max(top_remaining, bottom_remaining)
            min_second_robot = min(min_second_robot, second_robot)

        return min_second_robot
