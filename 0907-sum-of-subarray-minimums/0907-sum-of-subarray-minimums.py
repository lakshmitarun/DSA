class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        prv=[-1]*len(arr)
        stack=[]
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack:
                prv[i]=stack[-1]
            stack.append(i)
        nge=[len(arr)]*len(arr)
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if  stack:
                nge[i]=stack[-1]
            stack.append(i)
        total=0
        mod=10**9+7
        for j in range(len(arr)):
            left=j-prv[j]
            right=nge[j]-j
            total=(total+(left*right*arr[j])%mod)%mod
        return total    