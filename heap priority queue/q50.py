class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.mn = 1
        

    def popSmallest(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)
        self.mn += 1 
        return self.mn-1
        

    def addBack(self, num: int) -> None:
        if self.mn>num and num not in self.heap:
            heapq.heappush(self.heap,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)