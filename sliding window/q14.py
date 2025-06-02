def findMaxAverage(nums,k):
    csum= msum= sum(nums[:k])
    
    for i in range(k,len(nums)):
        csum += nums[i] - nums[i-k]
        
        msum= max(msum,csum)
    
    return msum/k

k=int(input())
nums= list(map(int, input().split()))
print(findMaxAverage(nums,k))