class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)

        answer = 0
        for letter in letters:
            l, r = s.index(letter), s.rindex(letter)

            answer += len(set(s[l + 1 : r]))

        return answer


solution = Solution()
a = solution.countPalindromicSubsequence("aabca")
b = solution.countPalindromicSubsequence("adc")
c = solution.countPalindromicSubsequence("bbcbaba")
print(a)
print(b)
print(c)
