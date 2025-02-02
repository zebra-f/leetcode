import string
from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        forward_shifts = [[0, 0] for _ in range(n)]
        backward_shifts = [[0, 0] for _ in range(n)]

        for shift in shifts:
            start, end, direction = shift
            if direction == 1:
                forward_shifts[start][0] += 1
                forward_shifts[end][1] += 1
            else:
                backward_shifts[start][0] += 1
                backward_shifts[end][1] += 1

        combined_shifts = [0] * n

        add = 0
        for i in range(n):
            starts, ends = forward_shifts[i]
            add += starts
            combined_shifts[i] += add
            add -= ends

        subtrackt = 0
        for i in range(n):
            starts, ends = backward_shifts[i]
            subtrackt += starts
            combined_shifts[i] -= subtrackt
            subtrackt -= ends

        alpha = list(string.ascii_lowercase)

        s_list = list(s)
        for i, shift in enumerate(combined_shifts):
            idx = alpha.index(s_list[i])
            if shift < 0:
                shift %= -26
                idx += shift
            elif shift > 0:
                shift %= 26
                idx += shift
                idx %= 26
            s_list[i] = alpha[idx]

        return "".join(s_list)


solution = Solution()
a = solution.shiftingLetters(s="abc", shifts=[[0, 1, 0], [1, 2, 1], [0, 2, 1]])
b = solution.shiftingLetters(s="dztz", shifts=[[0, 0, 0], [1, 1, 1]])
print(a)
print(b)
