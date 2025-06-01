def maxOperations(nums,k):
    nums.sort()
    l=0
    r=len(nums)-1
    
    count=0
    
    while l<r:
        if (nums[l]+nums[r]==k):
            l+=1
            r-=1
            
            count+=1
        
        elif (nums[l]+nums[r]<k):
            l+=1
        
        else:
            r-=1
    return count 

k = int(input())
nums = list(map(int, input().split()))
print(maxOperations(nums,k))