from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set(["a", "e", "i", "o", "u"])

        prefix = [0]
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])

        postfix = [0]
        for word in words[::-1]:
            if word[0] in vowels and word[-1] in vowels:
                postfix.append(postfix[-1] + 1)
            else:
                postfix.append(postfix[-1])
        postfix.reverse()

        answer = []
        for l, r in queries:
            diff = postfix[0] - postfix[l]
            answer.append(prefix[r + 1] - diff)
        return answer


solution = Solution()
a = solution.vowelStrings(
    words=["aba", "bcb", "ece", "aa", "e"], queries=[[0, 2], [1, 4], [1, 1]]
)
b = solution.vowelStrings(["a", "e", "i"], queries=[[0, 2], [0, 1], [2, 2]])
print(a)
print(b)
