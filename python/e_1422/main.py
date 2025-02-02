class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count("1")
        if s[0] == "1":
            ones -= 1
        zeroes = 1 if s[0] == "0" else 0
        answer = zeroes + ones
        for i in range(1, len(s) - 1):
            curr = int(s[i])
            if curr == 0:
                zeroes += 1
            if curr == 1:
                ones -= 1
            answer = max(answer, ones + zeroes)
        return answer


solution = Solution()
a = solution.maxScore("011101")
b = solution.maxScore("00111")
c = solution.maxScore("1111")
print(a)
print(b)
print(c)
