class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        answer = blocks[0:k].count("W")
        whites = answer

        l = 1
        r = k
        while r < len(blocks):
            if blocks[l - 1] == "W":
                whites -= 1
            if blocks[r] == "W":
                whites += 1
            answer = min(answer, whites)
            l += 1
            r += 1

        return answer


solution = Solution()
a = solution.minimumRecolors(blocks="WBBWWBBWBW", k=7)
print(a)
b = solution.minimumRecolors(blocks="WBWBBBW", k=2)
print(b)
