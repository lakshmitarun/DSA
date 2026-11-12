class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        pre=1
        while pre<len(arr) and arr[pre]>=arr[pre-1]:
            pre+=1
        if pre == len(arr):
            return 0
        sufix=len(arr)-2
        while sufix>=0 and arr[sufix]<=arr[sufix+1]:
            sufix-=1
        left=0
        right=sufix+1
        ans=min(sufix+1,len(arr)-pre)
        while left<pre and right<len(arr):
            if arr[left]<=arr[right]:
                ans=min(ans,right-left-1)
                left+=1
            else:
                right+=1
        return ans