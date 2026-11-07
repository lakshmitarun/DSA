class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        maxm=0
        sumn=0
        while left<right:
            sumn=nums[left]+nums[right]
            maxm=max(maxm,sumn)
            left+=1
            right-=1
        return maxm