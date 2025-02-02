from functools import cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 1_000_000_007

        @cache
        def cgs(i):
            if i > high:
                return 0
            answer = 1 if i >= low else 0
            answer += cgs(i + zero)
            answer += cgs(i + one)
            return answer % mod

        return cgs(0)


solution = Solution()
a = solution.countGoodStrings(low=3, high=3, zero=1, one=1)
b = solution.countGoodStrings(low=2, high=3, zero=1, one=2)
print(a)
print(b)
