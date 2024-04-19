#https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        traversed = {}
        def dfs(i,j):
            if (i,j) not in traversed:
                if 0 <= i < m and 0 <= j < n and grid[i][j]=="1":
                    traversed[(i,j)] = None
                    dfs(i+1,j)
                    dfs(i,j+1)
                    dfs(i-1,j)
                    dfs(i,j-1)
        count = 0
        for i in range(m):
            for j in range(n):
                if (i,j) not in traversed and grid[i][j]=="1":
                    dfs(i,j)
                    count +=1
        return count
