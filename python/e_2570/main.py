from typing import List


class Solution:
    def mergeArrays(
        self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        arr = []
        i1 = 0
        i2 = 0

        while i1 < len(nums1) and i2 < len(nums2):
            id1, val1 = nums1[i1]
            id2, val2 = nums2[i2]
            if id1 == id2:
                arr.append([id1, val1 + val2])
                i1 += 1
                i2 += 1
            elif id1 < id2:
                arr.append([id1, val1])
                i1 += 1
            else:
                arr.append([id2, val2])
                i2 += 1

        if i1 < len(nums1):
            arr.extend(nums1[i1:])
        if i2 < len(nums2):
            arr.extend(nums2[i2:])

        return arr


solution = Solution()
a = solution.mergeArrays(nums1=[[1, 2], [2, 3], [4, 5]], nums2=[[1, 4], [3, 2], [4, 1]])
print(a)
b = solution.mergeArrays(nums1=[[2, 4], [3, 6], [5, 5]], nums2=[[1, 3], [4, 3]])
print(b)
