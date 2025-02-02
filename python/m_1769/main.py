from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)

        counter = 0
        prefix = [0]
        for i in range(1, n + 1):
            prefix.append(counter + prefix[i - 1])
            if i < len(boxes) and boxes[i - 1] == "1":
                counter += 1

        counter = 0
        postfix = [0] * n + [0]
        for i in range(n - 1, -1, -1):
            postfix[i] = counter + postfix[i + 1]
            if i >= 0 and boxes[i] == "1":
                counter += 1

        answer = []
        for i in range(n):
            answer.append(prefix[i + 1] + postfix[i])

        return answer


solution = Solution()
a = solution.minOperations(boxes="110")
b = solution.minOperations(boxes="001011")
