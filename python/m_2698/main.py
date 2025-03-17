class Solution:
    def punishmentNumber(self, n: int) -> int:
        powers_of_ten = {10**i for i in range(10)}
        answer = 0
        for i in range(1, n + 1):
            square = i * i
            if square in powers_of_ten:
                answer += square
                continue

            is_equal = self.square_parts_sum_is_equal_to_i(square, i)
            if is_equal:
                answer += square

        return answer

    def square_parts_sum_is_equal_to_i(self, square: int, i: int) -> bool:
        square_str = str(square)

        def check(l, r, curr_sum) -> bool:
            if r == len(square_str):
                return curr_sum + int(square_str[l:r]) == i

            a = check(l, r + 1, curr_sum)
            b = check(r, r + 1, curr_sum + int(square_str[l:r]))

            return a or b

        return check(0, 1, 0)


solution = Solution()
a = solution.punishmentNumber(10)
print(a)
b = solution.punishmentNumber(37)
print(b)
