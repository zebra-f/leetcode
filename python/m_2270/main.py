from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum_ = sum(nums)
        answer = 0

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        prefix = prefix[1:]

        for i in range(n - 1):
            left_sum = prefix[i]
            right_sum = sum_ - left_sum
            if left_sum >= right_sum:
                answer += 1

        return answer


solution = Solution()
a = solution.waysToSplitArray([10, 4, -8, 7])
b = solution.waysToSplitArray([2, 3, 1, 0])
