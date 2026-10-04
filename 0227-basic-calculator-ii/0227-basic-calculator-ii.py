class Solution:
    def calculate(self, s: str) -> int:
        arr=[]
        nums=0
        sign="+"
        i=0
        while i<len(s):
            if s[i].isdigit():
                nums=nums*10+int(s[i])
            if (not s[i].isdigit() and s[i]!=" " )or i==len(s)-1:
                if sign=="+":
                    arr.append(+nums)
                elif sign=="-":
                    arr.append(-nums)
                elif sign=="*":
                    arr.append(arr.pop()*nums)
                elif sign=="/":
                    arr.append(int(arr.pop()/nums))
                sign=s[i]
                nums=0
            i+=1
        return sum(arr)                      
