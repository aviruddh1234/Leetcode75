def gcdofstrings(str1, str2):
    if str1+str2 != str2+str1:
        return ""
    def gcd(len1, len2):
        if len1==0:
            return len2
        return gcd(len2 % len1, len1)
    len1, len2 = len(str1), len(str2)

    return str1[:gcd(len1, len2)]
        