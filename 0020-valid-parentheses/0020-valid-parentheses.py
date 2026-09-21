class Solution:
    def isValid(self, s: str) -> bool:
        arr=[]
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                arr.append(s[i])
            else:
                if not arr:
                    return False
                ch=arr[-1]
                arr.pop()
                if s[i]==")" and ch=="(" or s[i]=="]" and ch=="[" or s[i]=="}" and ch=="{":
                    pass
                else:
                    return False
        if not arr:
            return True
        else:
            return False                          
