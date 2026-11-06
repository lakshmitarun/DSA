class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        left=0
        right=0
        maxm=0
        while left<len(nums1) and right<len(nums2):
            if nums1[left]<=nums2[right]:
                distance=right-left 
                maxm=max(maxm,distance)
                right+=1
            else:
                left+=1
        return maxm