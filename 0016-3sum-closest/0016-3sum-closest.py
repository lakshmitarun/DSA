class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        ans=float("inf")
        for i in range(len(nums)):
            low=i+1
            high=len(nums)-1
            while low<high:
                sum_=nums[i]+nums[low]+nums[high]
                deff=abs(sum_-target)
                if deff<abs(ans-target):
                    ans=sum_
                if sum_<target:
                    low+=1
                else:
                    high-=1
        return ans            