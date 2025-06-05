from collections import defaultdict

def equalpairs(grid):
    
    rf = defaultdict(int)
    
    for row in grid:
        row = tuple(row)
        rf[row] += 1 
        
    
    res = 0
    
    for col in zip(*grid):
        if col in rf:
            res += rf[col]
            
    return res 


            