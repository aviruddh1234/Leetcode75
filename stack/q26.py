def decodeString(s):
    stack = []
    currnum = 0
    currstr = ''
    
    for c in s:
        if c.isdigit():
            currnum = currnum*10 + int(c)
        
        elif c == '[':
            stack.append(currstr)
            stack.append(currnum)
            currstr = ''
            currnum = 0 
        
        elif c == ']':
            num = stack.pop()
            prevstr = stack.pop()
            currstr = prevstr + num*currstr
        
        else:
            currstr += c 
    
    return currstr 

s = input()
print(decodeString(s))
    