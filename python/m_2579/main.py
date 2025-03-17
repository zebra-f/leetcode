class Solution:
    def coloredCells(self, n: int) -> int:
        if n % 2 == 0:
            # square
            a = (n - 1) * (n - 1)
            b = 4 * (n // 2)
            # triangle
            side = (n // 2) - 1
            half_side = (side / 2) + 0.5
            c = (side * half_side * 2) * 4
        else:
            # square
            a = n * n
            b = 4 * (n // 2)
            # triangle
            side = (n // 2) - 1
            half_side = (side / 2) + 0.5
            c = (side * half_side * 2) * 4
        return int(a + b + c)


solution = Solution()
a = solution.coloredCells(1)
print(a)
b = solution.coloredCells(2)
print(b)
c = solution.coloredCells(3)
print(c)
d = solution.coloredCells(8)
print(d)
