import math
from functools import cache
from typing import List
from collections import defaultdict


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            sums.append(sums[-1] - nums[i - k] + nums[i])

        memo = defaultdict(lambda: defaultdict(float))

        def dp(i, taken):
            if taken == 3:
                return 0
            if i >= len(sums):
                return float("-inf")

            if memo[i][taken]:
                return memo[i][taken]

            with_current = sums[i] + dp(i + k, taken + 1)
            skip_current = dp(i + 1, taken)

            memo[i][taken] = max(with_current, skip_current)
            return memo[i][taken]

        dp(0, 0)

        indices = []

        def dfs(i, taken):
            if taken == 3 or i >= len(sums):
                return

            with_current = sums[i] + dp(i + k, taken + 1)
            skip_current = dp(i + 1, taken)

            if with_current >= skip_current:
                indices.append(i)
                dfs(i + k, taken + 1)
            else:
                dfs(i + 1, taken)

        dfs(0, 0)

        return indices


solution = Solution()
a = solution.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2)
# a = solution.maxSumOfThreeSubarrays([7, 13, 20, 19, 19, 2, 10, 1, 1, 19], 3)
b = solution.maxSumOfThreeSubarrays([1, 2, 1, 2, 1, 2, 1, 2, 1], 2)
print("\n", a, "\n", b)
