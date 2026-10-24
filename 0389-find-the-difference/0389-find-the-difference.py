class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=list(s)
        t=list(t)
        s.sort()
        t.sort()
        left=0
        right=0
        while left<len(s) and right<len(t):
            if s[left]!=t[right]:
                return t[right]
            left+=1
            right+=1
        return t[right]
