from functools import cache
from typing import List
import math


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        answer = -1

        left = values[0]
        for i, val in enumerate(values[1:]):
            right = val - (i + 1)
            answer = max(answer, left + right)
            left = max(left, val + i + 1)

        return answer


solution = Solution()
a = solution.maxScoreSightseeingPair([8, 1, 5, 2, 6])
b = solution.maxScoreSightseeingPair([8, 1, 1, 1, 5, 2, 6])
c = solution.maxScoreSightseeingPair([8, 1, 1, 1, 1, 1, 1, 5, 4, 1, 6])
d = solution.maxScoreSightseeingPair([1, 2])
print(a, "\n", b, "\n", c, "\n", d)
