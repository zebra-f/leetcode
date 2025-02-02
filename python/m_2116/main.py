class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        s_locked = []
        s_unlocked = []
        for i, char in enumerate(s):
            if locked[i] == "1":
                s_locked.append([i, char])
            else:
                s_unlocked.append([i, char])

        stack = []
        for i, char in s_locked:
            if char == "(":
                stack.append([i, char])
            else:
                if len(stack) > 0 and stack[-1][1] == "(":
                    stack.pop()
                else:
                    stack.append([i, char])

        if len(stack) == 0 and len(s_unlocked) % 2 == 1:
            return False
        elif len(stack) == 0 and len(s_unlocked) % 2 == 0:
            return True

        if len(s_unlocked) == 0:
            return False

        s_locked_right = []
        s_locked_left = []
        for i, char in stack:
            if char == "(":
                s_locked_left.append([i, char])
            else:
                s_locked_right.append([i, char])

        l = len(s_locked_left) - 1
        u = len(s_unlocked) - 1
        while l >= 0 and u >= 0:
            i1, _ = s_locked_left[l]
            i2, _ = s_unlocked[u]
            if i1 < i2:
                s_locked_left.pop()
                s_unlocked.pop()
            else:
                return False
            l -= 1
            u -= 1

        if s_locked_left:
            return False

        l = 0
        u = 0
        while l < len(s_locked_right) and u < len(s_unlocked):
            i1, _ = s_locked_right[l]
            i2, _ = s_unlocked[u]

            if i1 < i2:
                return False

            l += 1
            u += 1

        if l < len(s_locked_right):
            return False

        if (len(s_unlocked) - u) % 2 == 1:
            return False

        return True


solution = Solution()
a = solution.canBeValid(s="))()))", locked="010100")
print(a)
b = solution.canBeValid(s="()()", locked="0000")
print(b)
c = solution.canBeValid(s="((((())", locked="1111101")
print(c)
