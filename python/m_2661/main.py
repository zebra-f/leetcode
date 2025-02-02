from typing import List
from collections import defaultdict


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        num_map = defaultdict(list)
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                num = mat[i][j]
                num_map[num].append(i)
                num_map[num].append(j)
                row_map[i].add(num)
                col_map[j].add(num)

        for idx, i in enumerate(arr):
            row, col = num_map[i]
            row_map[row].remove(i)
            col_map[col].remove(i)
            if len(row_map[row]) == 0:
                return idx
            if len(col_map[col]) == 0:
                return idx

        return -1


soltution = Solution()
a = soltution.firstCompleteIndex(arr=[1, 3, 4, 2], mat=[[1, 4], [2, 3]])
print(a)
b = soltution.firstCompleteIndex(
    arr=[2, 8, 7, 4, 1, 3, 5, 6, 9], mat=[[3, 2, 5], [1, 4, 6], [8, 7, 9]]
)
print(b)
