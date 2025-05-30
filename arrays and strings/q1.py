def mergealter(word1,word2):
    res=""
    minlen=min(len(word1),len(word2))
    for i in range(minlen):
        res+=word1[i]
        res+=word2[i]
    
    res+=word1[minlen:]
    res+=word2[minlen:]
    return res

# Example usage:
print(mergealter("abc","def"))  # Output: "adbecf"