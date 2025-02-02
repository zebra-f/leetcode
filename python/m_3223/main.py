from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        removed = 0
        s_counter = Counter(s)
        for count in s_counter.values():
            if count > 2:
                if count & 1:
                    removed += count - 1
                else:
                    removed += count - 2
        return len(s) - removed


solution = Solution()
a = solution.minimumLength(s="abaacbcbb")
print(a)
b = solution.minimumLength(s="aa")
print(b)
