def uniqueoccurence(arr):
    res=[]
    
    freq ={}
    
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i] = 1
    
    for key, values in freq.items():
        res.append(values)
    
    return len(set(res)) == len(res)