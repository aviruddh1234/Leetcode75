def reversevowels(s):
    vowels = set('aeiouAEIOU')
    s = list(s)
    i=0
    j=len(s)-1

    while i < j:
        if s[i] not in vowels:
            i+=1
        if s[j] not in vowels:
            j-=1
        if s[i] in vowels and s[j] in vowels:
            s[i], s[j]= s[j], s[i]
            i+=1
            j-=1
    
    return "".join(s)

s=input("Enter a string: ")
print(reversevowels(s))  # Output: String with vowels reversed