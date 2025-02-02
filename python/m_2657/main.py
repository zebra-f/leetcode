from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        answer = []
        C = set()
        common = 0
        for i in range(len(A)):
            a = A[i]
            if a in C:
                common += 1
            C.add(a)
            b = B[i]
            if b in C:
                common += 1
            C.add(b)
            answer.append(common)

        return answer


solution = Solution()
a = solution.findThePrefixCommonArray(A=[1, 3, 2, 4], B=[3, 1, 2, 4])
print(a)
b = solution.findThePrefixCommonArray(A=[2, 3, 1], B=[3, 1, 2])
print(b)
