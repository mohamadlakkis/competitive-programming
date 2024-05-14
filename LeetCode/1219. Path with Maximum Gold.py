#https://leetcode.com/problems/path-with-maximum-gold/
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def X(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
                return 0
            gold = grid[i][j]
            grid[i][j] = 0
            max_gold = max(X(i+1, j), X(i-1, j), X(i, j+1), X(i, j-1))
            grid[i][j] = gold
            return gold + max_gold

        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, X(i, j))
        return max_gold
