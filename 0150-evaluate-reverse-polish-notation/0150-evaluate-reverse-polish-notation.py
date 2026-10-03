class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        i=0
        arr=[]
        while i<len(tokens):
            if tokens[i].lstrip("-").isdigit():
                arr.append(int(tokens[i]))
            else:
                t1=arr[-1]
                arr.pop()
                t2=arr[-1]
                arr.pop()
                if tokens[i]=="-":
                    arr.append(t2-t1)
                elif tokens[i]=="+":
                    arr.append(t1+t2)
                elif tokens[i]=="*":
                    arr.append(t1*t2)
                elif tokens[i]=="/":
                    arr.append(int(t2/t1))
            i+=1
        return arr[-1]    