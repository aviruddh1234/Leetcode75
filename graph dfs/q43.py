class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False]*n

        visit = [0]

        while visit:
            node = visit.pop()

            if visited[node]:
                continue 
            
            visited[node] = True
            visit.extend(rooms[node])
        
        return all(visited)