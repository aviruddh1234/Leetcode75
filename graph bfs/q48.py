class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0 
        fresh = 0 

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1 
                elif grid[i][j] == 2:
                    q.append([i,j])
        
        directions = [[1,0], [-1,0], [0,1], [0,-1]]

        while q and fresh>0:
            for i in range(len(q)):

                row,col = q.popleft()

                for dr, dc in directions:
                    r = row+dr 
                    c = col+dc 

                    if (r<0 or r == len(grid) or c<0 or c == len(grid[0]) or grid[r][c]!=1):
                        continue 
                    
                    grid[r][c] = 2
                    q.append([r,c])
                    fresh -= 1 
            
            time += 1 
        
        return time if fresh ==0 else -1 
        
        
