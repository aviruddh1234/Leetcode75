def longestSubarray(nums):
    l= 0 
    r = 0
    n = len(nums)
    zero = 0 
    z = 0 
    mx = 0 
    while r<n:
        if nums[r]==0:
            zero +=1 
                
            if zero >1: 
                mx = max(mx, r-l-1)
                                        
                l = z+1 
                    
                zero -=1 
            z = r 
        else: mx = max(mx, r-l) 
        r+=1 
            
    return mx