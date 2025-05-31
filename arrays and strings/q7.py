def productExceptSelf(nums):
    n=len(nums)

    res=[0]*n
    pref=[0]*n
    post=[0]*n

    pref[0]=nums[0]
    for i in range(1,n):
        pref[i]=pref[i-1]*nums[i]
    
    post[n-1]=nums[n-1]
    for i in range(n-2,-1,-1):
        post[i]=post[i+1]*nums[i]
    
    for i in range(n):
        if i==0:
            res[i]=post[i+1]
        
        elif i==n-1:
            res[i]=pref[i-1]
        
        else:
            res[i]=pref[i-1]*post[i+1]
    return res

nums= list(map(int,input("enter the list of the numbers").split())) 
print(productExceptSelf(nums))