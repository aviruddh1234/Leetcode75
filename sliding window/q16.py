def longestOnes(nums,k):
    res = 0 
    left = 0 
    right = 0 
    zcount = 0 
    
    while (right<len(nums)):
        if nums[right] == 0:
            zcount += 1 
        
        while (zcount>k):
            if nums[left] == 0:
                zcount -= 1 
            left += 1 
        
        if zcount <= k:
            res = max(res, right-left+1)
    
        right += 1
    return res