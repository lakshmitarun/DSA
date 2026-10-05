class MinStack:

    def __init__(self):
        self.val=[]
    def push(self, value: int) -> None:
        self.min_=value
        if not self.val:
            self.val.append((value,self.min_))
        else:
            self.min_=min(value,self.val[-1][1])
            self.val.append((value,self.min_))    
    def pop(self) -> None:
        self.val.pop()
    def top(self) -> int:
        return self.val[-1][0]
    def getMin(self) -> int:
        return self.val[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()