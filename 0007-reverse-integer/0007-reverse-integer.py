class Solution:
    def reverse(self, x: int) -> int:
        arr=[]
        if x<0:
            sign=-1
        else:
            sign=1
        x=abs(x)
        for i in str(x):
            arr.append(int(i))
        arr.reverse()
        ans=sign*int("".join(map(str,arr)))
        if ans<-2 **31 or ans>2**31-1:
            return 0
        return ans     
