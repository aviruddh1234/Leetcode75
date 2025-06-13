from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1/val))

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            
            visited.add(src)
            for neighbor, weight in graph[src]:
                if neighbor in visited:
                    continue
                result = dfs(neighbor, dst, visited)
                if result != -1.0:
                    return result * weight
            return -1.0

        results = []
        for a, b in queries:
            results.append(dfs(a, b, set()))

        return results
# Example usage:
# equations = [["a", "b"], ["b", "c"]]      