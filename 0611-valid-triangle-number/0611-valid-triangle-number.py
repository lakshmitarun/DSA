class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        left=0
        right=len(nums)-1
        mid=right-1
        count=0
        while right>=2:
            left=0
            mid=right-1
            while left<=mid:
                if nums[left]+nums[mid]>nums[right]:
                    count+=mid-left
                    mid-=1
                else:
                    left+=1
            right-=1
        return count