class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        
        for s in spells:
            left = 0 
            right = len(potions)-1
            index = len(potions)

            while left<=right:
                mid = (left+right)//2

                if s*potions[mid] >= success:
                    index = mid
                    right = mid -1 
                
                else:
                    left = mid+1
            
            res.append(len(potions)-index)
        
        return res 



        

        