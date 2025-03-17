from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                s.remove(num)
            else:
                s.add(num)

        return len(s) == 0


solution = Solution()
a = solution.divideArray(nums=[3, 2, 3, 2, 2, 2])
print(a)
b = solution.divideArray(nums=[1, 2, 3, 4])
print(b)
