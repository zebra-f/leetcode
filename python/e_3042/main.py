from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        answer = 0
        i = 1
        while i < len(words):
            word1 = words[i]
            j = 0
            while j < i:
                word2 = words[j]
                is_prefix_postifx = self.is_prefix(word2, word1) and self.is_postfix(
                    word2, word1
                )
                answer += is_prefix_postifx
                j += 1
            i += 1

        return answer

    def is_prefix(self, s1, s2):
        if len(s1) > len(s2):
            return False

        i = 0
        while i < len(s1):
            if s1[i] != s2[i]:
                return False
            i += 1

        return True

    def is_postfix(self, s1, s2):
        if len(s1) > len(s2):
            return False
        i = -1
        while i >= -(len(s1)):
            if s1[i] != s2[i]:
                return False
            i -= 1
        return True


solution = Solution()
a = solution.countPrefixSuffixPairs(words=["a", "aba", "ababa", "aa"])
print(a)
b = solution.countPrefixSuffixPairs(words=["pa", "papa", "ma", "mama"])
print(b)
c = solution.countPrefixSuffixPairs(words=["abab", "ab"])
print(c)
