def compress(chars):
    res=[]
    read=0

    while read<len(chars):
        char=chars[read]
        count=0

        while read<len(chars) and chars[read]==char:
            read+=1
            count+=1
        
        res.append(char)

        if count>1:
            res.extend(list(str(count)))

    chars[:]= res 

    return chars 

chars= list(map(str, input().split()))
print(compress(chars))