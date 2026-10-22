class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        left=0
        right=0
        res=[]
        res1=[]
        while left<len(s):
            if s[left]!="#":
                res.append(s[left])
            elif res:
                res.pop()
            left+=1
        while right<len(t):
            if t[right]!="#":
                res1.append(t[right])
            elif res1:
                res1.pop()
            right+=1
        if res==res1:
            return True
        else:
            return False