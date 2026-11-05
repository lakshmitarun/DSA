class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        ages.sort()
        left=0
        right=0
        count=0
        i=0
        while i<len(ages):
            age=ages[i]
            while left<len(ages) and ages[left]<=0.5*age+7:
                left+=1
            if right<left:
                right=left
            while right<len(ages) and ages[right]<=age:
                right+=1
            count+=max(0,right-max(left,i+1))
            count+=max(0,i-left)
            i+=1
        return count