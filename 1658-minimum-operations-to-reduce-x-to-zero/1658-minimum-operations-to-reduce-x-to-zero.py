class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total_sum=sum(nums)      
        max_sub=total_sum-x
        if max_sub==0:
            return len(nums)
        left=0
        right=0
        total=0
        max_len=0
        while right<len(nums):
            total+=nums[right]
            while total>max_sub and left<=right:
                total-=nums[left]
                left+=1
            if total==max_sub:
                max_len=max(max_len,right-left+1)
            right+=1
        ans=len(nums)-max_len
        if max_sub<0 or max_len==0:
            return -1
        return ans