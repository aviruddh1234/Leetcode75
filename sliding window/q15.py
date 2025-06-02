def maxVowels(s,k):
    s = list(s)
    vowels = set('aeiou')
    
    mvowel = cvowel = 0
    
    for i in s[:k]:
        if i in vowels:
            mvowel+=1
            cvowel+=1
    
    for i in range(k, len(s)):
        if s[i] in vowels:
            cvowel += 1 
        if s[i-k] in vowels:
            cvowel -= 1
        
        mvowel = max(mvowel, cvowel)
    return mvowel 

s= input()
k= int(input())
print(maxVowels(s,k))