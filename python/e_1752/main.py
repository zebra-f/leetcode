from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        count_changes = 0

        prev_num = nums[0]
        for num in nums[1:]:
            if num < prev_num:
                count_changes += 1
            prev_num = num

        if nums[-1] > nums[0]:
            count_changes += 1

        return count_changes < 2


solution = Solution()
a = solution.check(nums=[3, 4, 5, 1, 2])
print(a)
b = solution.check(nums=[2, 1, 3, 4])
print(b)
c = solution.check(nums=[1, 2, 3])
print(c)
