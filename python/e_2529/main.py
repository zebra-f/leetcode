import bisect
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l = bisect.bisect_left(nums, 0)
        r = bisect.bisect_right(nums, 0)
        return max(l, len(nums) - r)


solution = Solution()
a = solution.maximumCount(nums=[-2, -1, -1, 1, 2, 3])
print(a)
b = solution.maximumCount(nums=[-3, -2, -1, 0, 0, 1, 2])
print(b)
c = solution.maximumCount(nums=[5, 20, 66, 1314])
print(c)
