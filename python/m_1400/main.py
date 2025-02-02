from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False

        counter = Counter(s)

        odd_nums = 0
        for char, count in counter.items():
            if count & 1:
                odd_nums += 1

        return False if odd_nums > k else True


solution = Solution()
a = solution.canConstruct(s="annabelle", k=2)
b = solution.canConstruct(s="leetcode", k=3)
c = solution.canConstruct(s="true", k=4)
print(a)
print(b)
print(c)
