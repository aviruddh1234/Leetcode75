def closeStrings(word1, word2):
    def counter(word):
        freq = {}
        
        for i in list(word):
            if i in freq:
                freq[i] += 1 
            else:
                freq[i] = 1
        
        return freq 

    freq1 = counter(word1)
    freq2 = counter(word2)
    
    return set(freq1.keys()) == set(freq2.keys()) and sorted(freq1.values()) == sorted(freq2.values())

word1 = input()
word2 = input()

print(closeStrings(word1,word2))