from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        colors = colors + colors
        answer = 0
        curr_length = 1
        l = 0
        r = 1
        while l < n:
            if colors[r - 1] != colors[r]:
                curr_length += 1
            else:
                curr_length = 1
                l = r
            r += 1
            if r - l == k:
                answer += 1
                l += 1

        return answer


solution = Solution()
a = solution.numberOfAlternatingGroups(colors=[0, 1, 0, 1, 0], k=3)
print(a)
b = solution.numberOfAlternatingGroups([0, 1, 0, 0, 1, 0, 1], k=6)
print(b)
c = solution.numberOfAlternatingGroups([1, 1, 0, 1], k=4)
print(c)
