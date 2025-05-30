def canplaceflowers(flowerbed,n):
    for i in range(len(flowerbed)):
        left= i==0 or flowerbed[i-1]==0
        right= i==len(flowerbed)-1 or flowerbed[i+1]==0

        if flowerbed[i]==0 and left and right:
            flowerbed[i]=1
            n-=1
    
    return n<=0

n=int(input("Enter the number of flowers to plant: "))
flowerbed= list(map(int, input("Enter the flowerbed (0s and 1s): ").split()))
print(canplaceflowers(flowerbed, n))  # Output: True or False based on the input