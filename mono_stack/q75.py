class StockSpanner:

    def __init__(self):
        self.mstack = []
        

    def next(self, price: int) -> int:
        stack = self.mstack 
        cq, cs = price, 1 

        while stack and stack[-1][0] <= cq:
            pq, ps = stack.pop()

            cs += ps 
        
        stack.append((cq, cs))

        return cs
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)