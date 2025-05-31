def reversewords(s):
    s=s.split()
    s=list(s)
    return " ".join(s[::-1])

s=input("Enter a string: ")
print(reversewords(s))  # Output: String with words reversed