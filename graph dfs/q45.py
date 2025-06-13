from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in connections:
            graph[a].append((b, True))   
            graph[b].append((a, False))  

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            count = 0
            for neighbor, needs_reversal in graph[node]:
                if not visited[neighbor]:
                    if needs_reversal:
                        count += 1
                    count += dfs(neighbor)
            return count

        return dfs(0)
