from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_xor = 0
        for num in nums1:
            nums1_xor ^= num

        nums3_xor_list = []
        for num in nums2:
            nums3_xor_list.append(num ^ nums1_xor)

        nums3_xor = 0
        for num in nums3_xor_list:
            nums3_xor ^= num

        return nums3_xor


solution = Solution()
a = solution.xorAllNums(nums1=[2, 1, 3], nums2=[10, 2, 5, 0])
print(a)
b = solution.xorAllNums(nums1=[1, 2], nums2=[3, 4])
print(b)
