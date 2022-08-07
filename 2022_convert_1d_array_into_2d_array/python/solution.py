from typing import List


class Solution:
    def construct2DArray(self, original: List[int], cols: int, rows: int) -> List[List[int]]:
        if rows * cols != len(original):
            return []

        result = []

        start = 0
        end = rows

        while end < rows * cols + 1:
            result.append(original[start:end])
            start = end
            end = end + rows

        return result
