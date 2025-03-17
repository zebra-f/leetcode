from functools import cache


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        powers_of_three = []
        i = 0
        while True:
            y = 3**i
            if y > n:
                break
            powers_of_three.append(y)
            i += 1

        # @cache
        # def number_is_sum_of_powers(i, sum):
        #     if sum == n:
        #         return True
        #     if sum > n or i >= len(powers_of_three):
        #         return False
        #     return number_is_sum_of_powers(
        #         i + 1, sum + powers_of_three[i]
        #     ) or number_is_sum_of_powers(i + 1, sum)

        curr = n
        for i in range(len(powers_of_three) - 1, -1, -1):
            if powers_of_three[i] <= curr:
                curr -= powers_of_three[i]
            if curr == 0:
                return True

        return True if curr == 0 else False


solution = Solution()
a = solution.checkPowersOfThree(12)
print(a)
b = solution.checkPowersOfThree(91)
print(b)
c = solution.checkPowersOfThree(21)
print(c)
d = solution.checkPowersOfThree(10_000_000)
print(d)
