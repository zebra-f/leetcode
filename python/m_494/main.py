from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def ftsm(i, curr):
            if i == len(nums):
                if curr == target:
                    return 1
                else:
                    return 0

            return ftsm(i + 1, curr + nums[i]) + ftsm(i + 1, curr - nums[i])

        answer = ftsm(0, 0)
        return answer


solution = Solution()
a = solution.findTargetSumWays([1, 1, 1, 1, 1], 3)
b = solution.findTargetSumWays([1], 1)
print(a)
print(b)
