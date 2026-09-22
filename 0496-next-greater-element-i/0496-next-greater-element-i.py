class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        arr=[]
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                one=nums2.index(nums1[i])
                for j in range(one+1,len(nums2)):
                    if nums2[j]>nums1[i]:
                        arr.append(nums2[j])
                        break
                else:
                    arr.append(-1)
        return arr                    