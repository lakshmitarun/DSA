class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        count=0
        if k==0:
            i=1
            while i<len(nums):
                if nums[i]==nums[i-1]:
                    count+=1
                    while i<len(nums) and nums[i]==nums[i-1]:
                        i+=1
                else:
                    i+=1
            return count
        left=0
        right=1
        while right<len(nums):
            if left==right:
                right+=1
                continue
            deff= abs(nums[left]-nums[right])
            if deff>k:
                left+=1
            elif deff<k:
                right+=1
            else:
                count+=1
                left+=1
                right+=1
                while left<len(nums) and nums[left]==nums[left-1]:
                    left+=1
                while right<len(nums) and nums[right]==nums[right-1]:
                    right+=1
        return count