def maxarea(height):
    res = 0 
    left = 0
    right = len(height)-1

    while left<right:
        area = min(height[left],height[right])*(right-left)
        res = max(area,res)

        if height[left]>height[right]:
            right-=1
        else:
            left+=1
    return res

height = list(map(int,input().split()))
print(maxarea(height))