def largestaltitude(gain):
    res = []
    
    for i in range(len(gain)):
        if i == 0:
            res.append(gain[i])
        else:
            res.append(gain[i]+res[i-1])
    
    return max(res)

gain = list(map(int, input().split()))
print(largestaltitude(gain))