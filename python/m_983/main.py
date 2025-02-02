from functools import cache
import bisect
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        @cache
        def mt(day):
            if day > days[-1]:
                return 0

            i = bisect.bisect_left(days, day)
            day = days[i]

            answer = float("inf")
            answer = min(answer, costs[0] + mt(day + 1))
            answer = min(answer, costs[1] + mt(day + 7))
            answer = min(answer, costs[2] + mt(day + 30))

            return answer

        answer = mt(days[0])
        return int(answer) if answer != float("inf") else int(answer)


solution = Solution()
a = solution.mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15])
b = solution.mincostTickets(
    days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]
)
print(a)
print(b)
