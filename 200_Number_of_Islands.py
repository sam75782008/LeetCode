from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        if not len(grid[0]):
            return 1
            
        self.m = len(grid)
        self.n = len(grid[0])
        self.pool = grid.copy()
        q = deque()
        for i in range(self.m):
            for j in range(self.n):
                if int(self.pool[i][j])==1:
                    self.pool[i][j]='0'
                    q.append([i,j])
                    self.helper_bfs([i,j])

        return len(q)
    
    def helper_bfs(self,pos):
        cur_y, cur_x = pos
        next_step = [[cur_y,cur_x+1],[cur_y,cur_x-1],[cur_y+1,cur_x],[cur_y-1,cur_x]]
        for k in range(4):
            yp, xp = next_step[k]
            if (0<=xp<=self.n-1) and (0<=yp<=self.m-1) and int(self.pool[yp][xp])==1:
                self.pool[yp][xp]='0'
                self.helper_bfs(next_step[k])

        
        