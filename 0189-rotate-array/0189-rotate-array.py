class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k=k%len(nums)
        nums.reverse()
        left=0
        right=k-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
        left=k
        right=len(nums)-1
        while left<=right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
