def kidwithextracandies(candies, extracandies):
    result=[]
    m= max(candies)
    for i in candies:
        result.append(i+extracandies>=m)
    return result 

kidwithextracandies([2,3,4,1],3)