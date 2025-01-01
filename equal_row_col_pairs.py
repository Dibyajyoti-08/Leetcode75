class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        count = 0
        rows = defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1
        for col in range(len(grid)):
            colm = tuple(grid[r][col] for r in range(len(grid)))
            if colm in rows:
                count += rows[colm]
        return count