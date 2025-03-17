from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        answer = []
        zeroes = 0
        for i in range(len(nums) - 1):
            a = nums[i]
            b = nums[i + 1]
            if a == b:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
            if nums[i] == 0:
                zeroes += 1
            else:
                answer.append(nums[i])

        return answer + [nums[-1]] + ([0] * zeroes)


solution = Solution()
a = solution.applyOperations([1, 2, 2, 1, 1, 0])
print(a)
b = solution.applyOperations([0, 1])
print(b)
