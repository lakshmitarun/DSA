class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        nge=[len(heights)]*len(heights)
        stack=[]
        maxone=0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                ele=stack.pop()
                nge=i
                if not stack:
                    prv=-1
                else:
                    prv=stack[-1]
                maxone=max(maxone,heights[ele]*(nge-prv-1))
            stack.append(i)
        while stack:
                ele=stack.pop()
                nge=len(heights)
                if not stack:
                    prv=-1
                else:
                    prv=stack[-1]
                maxone=max(maxone,heights[ele]*(nge-prv-1))
        return maxone       

