class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        count = 0

        for i in range(1, n + 1):
            if i != n and prefix[n] <= 2 * prefix[i]:
                count += 1
        return count
