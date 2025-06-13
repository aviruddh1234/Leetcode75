class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(city, visited):

            stack = [city]

            while stack:

                curr = stack.pop()

                if not visited[curr]:
                    visited[curr] = True 

                    for j in range(len(isConnected)):
                        
                        if isConnected[curr][j] == 1 and not visited[j]:
                            stack.append(j)
        
        n= len(isConnected)
        visited = [False] * n
        res = 0

        for city in range(n):
            if not visited[city]:
                dfs(city, visited)

                res += 1 
        
        return res

            
                

        
        