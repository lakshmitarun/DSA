class StockSpanner:

    def __init__(self):
        self.arr=[]
        self.prg=[]
        self.stack=[]
    def next(self, price: int) -> int:
        self.arr.append(price)
        self.cur=len(self.arr)-1
        while self.stack and self.arr[self.stack[-1]]<=price:
            self.stack.pop()
        if not self.stack:
            self.prg=-1
        else:
            self.prg=self.stack[-1]
        span= self.cur-self.prg
        self.stack.append(self.cur)
        return span    




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)