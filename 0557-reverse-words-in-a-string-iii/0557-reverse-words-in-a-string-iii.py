class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s)
        left=0
        while left<len(s):
            right=left
            while right<len(s) and s[right]!=" ":
                right+=1
            right-=1
            end=right
            while left<right:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
            left=end+2
        return "".join(s)
