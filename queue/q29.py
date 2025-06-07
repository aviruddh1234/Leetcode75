from collections import deque

def predictvictory(senate):
    
    res = deque(senate)
    count = 0 
    
    while True:
        rcount = 0 
        dcount = 0 
        
        newq = deque()
        
        n = len(res)
        
        for _ in range(n):
            ch = res.popleft()
            
            if ch == 'R':
                if count < 0:
                    count += 1 
                    continue
                
                else:
                    count += 1 
                    rcount += 1 
                    newq.append('R')
            
            else:
                if count > 0:
                    count -= 1
                    continue
                
                else:
                    count -= 1 
                    dcount += 1 
                    newq.append('D')
        
        if rcount == 0:
            return 'Dire'
        
        if dcount == 0:
            return 'Radiant'
        
        res = newq

senate = input()
print(predictvictory(senate))
