def issubsequence(s,t):
    if not s:
        return True 

    if s and not t:
        return False 
    
    p1=0
    p2=0
    while p2<len(t):
        if p1<len(s) and s[p1]==t[p2]:
            p1+=1
        p2+=1
    
    return p1==len(s)

s=input()
t=input()
print(issubsequence(s,t))