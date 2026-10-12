class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        high=[0]*m
        maxone=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=="1":
                    high[j]+=1
                else:
                    high[j]=0
            stack=[]
            for i in range(len(high)):
                while stack and high[stack[-1]]>high[i]:
                    ele=stack.pop()
                    if not stack:
                        prv=-1
                    else:
                        prv=stack[-1]
                    maxone=max(maxone,high[ele]*(i-prv-1))
                stack.append(i)
            while stack:
                    ele=stack.pop()
                    if not stack:
                        prv=-1
                    else:
                        prv=stack[-1]
                    maxone=max(maxone,high[ele]*(m-prv-1))
        return maxone