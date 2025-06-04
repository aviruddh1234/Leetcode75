def pivotindex(nums):
    right = sum(nums)
    left = 0 
    
    for i in range(len(nums)):
        right -= nums[i]
        if left == right:
            return i
        left += nums[i]
    
    return -1 

nums = list(map(int, input().split()))
print(pivotindex(nums))