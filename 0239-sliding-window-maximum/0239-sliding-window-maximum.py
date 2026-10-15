class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        from collections import deque
        stack=[]
        d=deque()
        for i in range(len(nums)):
            if d and d[0]<=i-k:
                d.popleft()
            while d and nums[d[-1]]<=nums[i]:
                d.pop()
            d.append(i)
            if i>=k-1:
                stack.append(nums[d[0]])
        return stack