class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name=list(name)
        typed=list(typed)
        left=0
        right=0
        while left<len(name) and right<len(typed):
            if name[left]==typed[right]:
                left+=1
                right+=1
            elif right>0 and typed[right]==typed[right-1]:
                right+=1
            else:
                return False
        while right<len(typed) and right>0 and typed[right]==typed[right-1]:
            right+=1
        if left==len(name) and right==len(typed):
            return True
        else:
            return False