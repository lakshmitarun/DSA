class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        arr.sort()
        mod=10**9+7
        count=0
        for i  in range(len(arr)-2):
            left=i+1
            right=len(arr)-1
            while left<right:
                total=arr[i]+arr[left]+arr[right]
                if total<target:
                    left+=1
                elif total>target:
                    right-=1
                else:
                    if arr[left]!=arr[right]:
                        leftcount=1
                        rightcount=1
                        while left+1 <right and arr[left]==arr[left+1]:
                            leftcount+=1
                            left+=1
                        while right-1>left and arr[right]==arr[right-1]:
                            rightcount+=1
                            right-=1
                        count+=leftcount*rightcount
                    else:
                        n=right-left+1
                        count+=n*(n-1)//2
                        break
                    left+=1
                    right-=1
        return count%mod