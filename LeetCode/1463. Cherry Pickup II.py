class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        D = {}
        def X(r,c1,c2):
            if(r,c1,c2)in D:
                return D[(r,c1,c2)]
            if(c1==c2) or  min(c1,c2)<0 or max(c1,c2)>=COLS:
                return 0
            if r==ROWS-1:
                return grid[r][c1]+grid[r][c2]
            MAX= 0
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    MAX = max(MAX,X(r+1,c1+i,c2+j))
            
            MAX+=grid[r][c1]+grid[r][c2]
            D[(r,c1,c2)] = MAX
            return MAX
        return X(0,0,COLS-1)
