class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        m = len(maze)
        n = len(maze[0])

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        q = deque()
        q.append((entrance[0], entrance[1], 0))
        maze[entrance[0]][entrance[1]] = '+'

        while q:
            row, col , steps = q.popleft()

            for dr, dc in directions:
                r,c = row + dr, col + dc 


                if 0<=r<m and 0<=c<n and maze[r][c] == ".":
                    if r == 0 or r == m-1 or c == 0 or c == n-1:
                        return steps+1
                

                    maze[r][c] = '+'
                    q.append((r,c, steps+1))
        return -1

        