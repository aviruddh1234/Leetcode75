def singleNumber(nums):
    xor = 0 
    
    for num in nums:
        xor ^= num 
    
    return xor 

nums = list(map(int, input().split()))
print(singleNumber(nums))