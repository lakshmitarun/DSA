class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        prev=[-1]*len(nums)
        stack=[]
        for i in range(len(nums)):
            while stack and nums[stack[-1]]>nums[i]:
                stack.pop()
            if stack:
                prev[i]=stack[-1]
            stack.append(i)
        nge=[len(nums)]*len(nums)
        stack=[]
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            if stack:
                nge[i]=stack[-1]
            stack.append(i)
        sum_min=0
        mod=10**9+7
        for i in range(len(nums)):
            left=i-prev[i]
            right=nge[i]-i
            sum_min=(sum_min+left*right*nums[i])
        prev=[-1]*len(nums)
        stack=[]
        for i in range(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                stack.pop()
            if stack:
                prev[i]=stack[-1]
            stack.append(i)
        nge=[len(nums)]*len(nums)
        stack=[]
        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop()
            if stack:
                nge[i]=stack[-1]
            stack.append(i)
        sum_max=0
        mod=10**9+7
        for i in range(len(nums)):
            left=i-prev[i]
            right=nge[i]-i
            sum_max=(sum_max+left*right*nums[i])
        return sum_max-sum_min        