class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        word=set()
        left=0
        sumn=0
        maxone =0
        for i in range(len(nums)):
            while nums[i] in word:
                word.remove(nums[left])
                sumn= sumn-nums[left]
                left+=1    
            word.add(nums[i])
            sumn=sumn+nums[i]
            maxone= max(maxone,sumn)
        return maxone   
               
                
                
        