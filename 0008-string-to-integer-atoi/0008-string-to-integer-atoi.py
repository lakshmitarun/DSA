class Solution:
    def myAtoi(self, s: str) -> int:
        arr=[]
        left=0
        while left<len(s) and s[left]==" ":
            left+=1
        sign=1
        if left<len(s) and s[left]=="-":
            sign=-1
            left+=1
        elif left<len(s) and s[left]=="+":
            left+=1
        arr=[]
        while left<len(s) and s[left].isdigit():
            arr.append(s[left])
            left+=1
        if not arr:
            return 0
        ans=0
        for i in arr:
            ans=ans*10+(ord(i)-ord("0"))
        ans=sign*ans
        if ans<-2**31:
            return -2**31
        if ans>2**31-1:
            return 2**31-1
        return ans   
