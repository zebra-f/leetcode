from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        for word1 in words:
            for word2 in words:
                if word1 == word2:
                    continue
                if word1 in word2:
                    answer.append(word1)
        return list(set(answer))


solution = Solution()
a = solution.stringMatching(words=["mass", "as", "hero", "superhero"])
print(a)
b = solution.stringMatching(words=["leetcode", "et", "code"])
print(b)
