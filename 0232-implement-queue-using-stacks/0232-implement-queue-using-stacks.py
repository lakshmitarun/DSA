class MyQueue:

    def __init__(self):
        self.input=[]
        self.output=[]
    def push(self, x: int) -> None:
        self.input.append(x)
    def pop(self) -> int:
        if self.output:
            return self.output.pop()
        else:
            while self.input:
                self.output.append(self.input.pop())
            return self.output.pop()   
    def peek(self) -> int:
        if self.output:
            return self.output[-1]
        else:
            while self.input:
                self.output.append(self.input.pop())
            return self.output[-1] 
    def empty(self) -> bool:
        return not self.input and not self.output


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()