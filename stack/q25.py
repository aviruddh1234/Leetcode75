def astroidCollsision(astroids):
    
    res = []
    
    for a in astroids:
        
        while res and a<0<res[-1]:
            if -a > res[-1]:
                res.pop()
                continue 
                
            elif -a == res[-1]:
                res.pop()
                
            break 
        else:
            res.append(a)
    

astroids = list(map(int, input().split()))
print(astroidCollsision(astroids))