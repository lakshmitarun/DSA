class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        left=0
        right=0
        res=[]
        while left<len(firstList) and right<len(secondList):
            start=max(firstList[left][0],secondList[right][0])
            end=min(firstList[left][1],secondList[right][1])
            if firstList[left][1]<secondList[right][1]:
                left+=1
            else:
                right+=1
            if start<=end:
                res.append([start,end])
        return res
        