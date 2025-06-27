class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0 
        
        points.sort(key = lambda x: x[1])

        curr = points[0][1]

        arrows = 0 

        for i in range(1, len(points)):
            if curr >= points[i][0]:
                continue 
            
            else:
                arrows += 1 
                curr = points[i][1]
        
        return arrows+1