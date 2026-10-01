class Solution:
    def romanToInt(self, s: str) -> int:
        arr=[]
        for i in range(len(s)):
            arr.append(s[i])
        total =0
        for j in range(len(arr)):
            if arr[j]=="I":
                value=1
            elif arr[j]=="V":
                value=5
            elif arr[j]=="X":
                value=10
            elif arr[j]=="L":
                value=50
            elif arr[j]=="C":
                value=100
            elif arr[j]=="D":
                value=500
            elif arr[j]=="M":
                value=1000
            if j<len(arr)-1:
                if arr[j + 1] == "I":
                    next_value = 1
                elif arr[j + 1] == "V":
                    next_value = 5
                elif arr[j + 1] == "X":
                    next_value = 10
                elif arr[j + 1] == "L":
                    next_value = 50
                elif arr[j + 1] == "C":
                    next_value = 100
                elif arr[j + 1] == "D":
                    next_value = 500
                elif arr[j + 1] == "M":
                    next_value = 1000 
                if value<next_value:
                    total-=value
                else:
                    total+=value
            else:
                total+=value
        return total                    