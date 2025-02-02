from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        answer = 0
        for word in words:
            if len(word) >= len(pref):
                answer += word[: len(pref)] == pref
        return answer


solution = Solution()
a = solution.prefixCount(words=["pay", "attention", "practice", "attend"], pref="at")
b = solution.prefixCount(words=["leetcode", "win", "loops", "success"], pref="code")
print(a, b)
