from typing import List


class Solution:
    size = (0,0)
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.size = (len(grid[0]),len(grid))
        return self.dp(grid)

    def dp(self, grid: List[List[int]]) -> int:
        start = (0,0)
        end = (0,0)
        total = 0
        for y, line in enumerate(grid):
            for x, i in enumerate(line):
                if i == 1:
                    start = (x,y)
                elif i == 2:
                    end = (x,y)
                else:
                    total += i
        if abs(start[0]-end[0]) + abs(start[1]-end[1]) == 1 and total == -self.size[0]*self.size[1]+2:
            return 1
        # Go left
        left = 0
        if(start[0]>0 and grid[start[1]][start[0]-1]==0):
            grid[start[1]][start[0]] = -1
            grid[start[1]][start[0]-1] = 1
            left = self.dp(grid)
            grid[start[1]][start[0]] = 1
            grid[start[1]][start[0]-1] = 0
        # Go right
        right = 0
        if(start[0]<self.size[0]-1 and grid[start[1]][start[0]+1]==0):
            grid[start[1]][start[0]] = -1
            grid[start[1]][start[0]+1] = 1
            right = self.dp(grid)
            grid[start[1]][start[0]] = 1
            grid[start[1]][start[0]+1] = 0
        # Go up
        up = 0
        if(start[1]>0 and grid[start[1]-1][start[0]]==0):
            grid[start[1]][start[0]] = -1
            grid[start[1]-1][start[0]] = 1
            up = self.dp(grid)
            grid[start[1]][start[0]] = 1
            grid[start[1]-1][start[0]] = 0
        # Go down
        down = 0
        if(start[1]<self.size[1]-1 and grid[start[1]+1][start[0]]==0):
            grid[start[1]][start[0]] = -1
            grid[start[1]+1][start[0]] = 1
            down = self.dp(grid)
            grid[start[1]][start[0]] = 1
            grid[start[1]+1][start[0]] = 0
        return left + right + up + down

sol = Solution()
print(sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
print(sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
print(sol.uniquePathsIII([[0,1],[2,0]]))