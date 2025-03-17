import math
from typing import List


class Solution:
    def is_primt_number(self, num):
        if num == 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def closestPrimes(self, left: int, right: int) -> List[int]:
        answer = [-1, -1]
        prime_numbers_in_range = []
        for num in range(left, right + 1):
            if self.is_primt_number(num):
                prime_numbers_in_range.append(num)

        if len(prime_numbers_in_range) < 2:
            return answer

        min_difference = math.inf
        for i in range(1, len(prime_numbers_in_range)):
            a = prime_numbers_in_range[i]
            b = prime_numbers_in_range[i - 1]
            diff = a - b
            if diff < min_difference:
                min_difference = diff
                answer = [b, a]

        return answer


solution = Solution()
a = solution.closestPrimes(left=10, right=19)
print(a)
b = solution.closestPrimes(left=4, right=6)
print(b)
