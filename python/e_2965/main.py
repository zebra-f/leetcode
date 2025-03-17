from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = [0] * len(grid) * len(grid)
        print(arr)
        answer = [-1, -1]
        for list_ in grid:
            for num in list_:
                arr[num - 1] += 1
                if arr[num - 1] == 2:
                    answer[0] = num

        print(arr)
        for i, num in enumerate(arr):
            if num == 0:
                answer[1] = i + 1
                break

        return answer


solution = Solution()
a = solution.findMissingAndRepeatedValues(grid=[[1, 3], [2, 2]])
print(a)
b = solution.findMissingAndRepeatedValues(grid=[[9, 1, 7], [8, 9, 2], [3, 4, 6]])
print(b)
