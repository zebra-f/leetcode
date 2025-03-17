class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        n = len(part)
        i = 0
        while i < len(s) - n + 1:
            if s[i : i + n] == part:
                s = s[0:i] + s[i + n :]
                i = 0
                continue
            i += 1

        return s


solution = Solution()
a = solution.removeOccurrences(s="daabcbaabcbc", part="abc")
print(a)
b = solution.removeOccurrences(s="axxxxyyyyb", part="xy")
print(b)
