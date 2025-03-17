from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l_pivot_arr = []
        m_pivot_arr = []
        r_pivot_arr = []

        for num in nums:
            if num < pivot:
                l_pivot_arr.append(num)
            if num == pivot:
                m_pivot_arr.append(num)
            if num > pivot:
                r_pivot_arr.append(num)

        return l_pivot_arr + m_pivot_arr + r_pivot_arr


solution = Solution()
a = solution.pivotArray(nums=[9, 12, 5, 10, 14, 3, 10], pivot=10)
print(a)
b = solution.pivotArray(nums=[-3, 4, 3, 2], pivot=2)
print(b)
