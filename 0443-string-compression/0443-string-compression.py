class Solution:
    def compress(self, chars: list[str]) -> int:
        s=[]
        left=0
        right=1
        while right<=len(chars):
            if right==len(chars) or chars[left]!=chars[right]:
                s.append(chars[left])
                count=right-left
                if count>1:
                    s.extend(str(count))
                    count=0
                left=right
            right+=1
        chars[:]=s
        return len(s)
    
